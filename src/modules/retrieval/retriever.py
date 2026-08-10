'''
Act as an orchestration that takes a raw search string, tell the embedder to create
a query vector, ask the vector store for a similarity search, and handles nested
ChromaDB into specified schemas.   
--  
(retrieval strategy)
Responsible for deciding how to retrieve useful context for downstream AI tasks.
It asks the embedder for a vector, decide what to query for, map the output 
from vector_store to SearchResult dataclass. 
Future: reranking (cohere or cross-encoders) or hybrid search 
'''
from typing import List

from src.modules.document.schema import Chunk
from src.modules.retrieval.schema import Embeddings, RetrievedChunk
from src.modules.retrieval.embedder import TextEmbedder
from src.modules.retrieval.vector_store import VectorStore

class TextRetriever:
    def __init__(self, embedder: TextEmbedder, store: VectorStore) -> None:
        '''
        Retriever sits on top of embedder and vector store to execute the search
        and ranking strategies.
        '''
        self.embedder = embedder
        self.store = store

    def retrieve(self, query_text: str, top_k: int=3) -> List[RetrievedChunk]:
        '''
        1. Turn raw search string into query vector.
        2. Query the vector database.
        3. Process the raw nested Chroma Dict into RetrievedChunk.
        '''
        query_vector = self.embedder.embed_query(query_text)

        raw_results = self.store.query_vectors(query_vector, top_k=top_k)

        retrieved_chunks: List[RetrievedChunk] = []

        if not raw_results or not raw_results["ids"]: # later on check if empty [[]]
            return retrieved_chunks

        ids = raw_results["ids"][0]  # see the section at the bottom for ChromaDB structure
        documents = raw_results["documents"][0]
        metadatas = raw_results["metadatas"][0]
        distances = raw_results["distances"][0]

        for idx, emb_chunk_id in enumerate(ids):
            metadata = metadatas[idx]
            
            chunk = Chunk(
                id=emb_chunk_id.split("::")[-1], # reconstruct a clean, original chunk_id 
                text=documents[idx],
                page_number=metadata["page_number"],
                source=metadata["source"]
            )

            retrieved_chunks.append(
                RetrievedChunk(
                    chunk=chunk,
                    score=distances[idx]
                )
            )

        # Placeholder: passing reranking function 

        return retrieved_chunks



####### Some ChromaDB output structure #######
'''
raw_results["ids"] = [
    # INDEX: This inner list contains ALL top_k matches with argument top_k
    [
        "paper.pdf_page1_chunk0",  # Match 1 (Closest)
        "paper.pdf_page4_chunk2",  # Match 2
        "paper.pdf_page2_chunk1"   # Match 3
    ]
]

'''