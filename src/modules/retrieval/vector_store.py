
from typing import List, Dict, Any #, cast
from pathlib import Path
import chromadb

# Import Chroma's internal types to satisfy the type checker
# from chromadb.api.types import Embeddings as ChromaEmbeddings, Metadatas as ChromaMetadatas

from src.modules.document.schema import Chunk
from src.modules.retrieval.schema import Embeddings

PROJECT_ROOT = Path(__file__).resolve().parents[3]

class VectorStore:
    '''
    Store and search vectors.
    '''
    def __init__(self, collection_name: str = "pdf_chunks") -> None:
        db_path = PROJECT_ROOT / "data" / "chroma"
        self.client = chromadb.PersistentClient(path=str(db_path))
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def save_to_chroma(self, 
                       chunks: List[Chunk], 
                       embeddings: List[Embeddings]) -> None:
        '''
        Save generated embeddings into vector database
        '''
        if not chunks or not embeddings: # safety check
            return 

        embeddings_map = {record.chunk_id: record for record in embeddings}

        ids: List[str] = []
        docText: List[str] = []
        vectors: List[List[float]] = []
        metadatas: List[Dict[str, Any]] = []

        for chx in chunks:
            emb_chunk_id = f"{chx.source}::{chx.id}"

            if emb_chunk_id in embeddings_map:
                record = embeddings_map[emb_chunk_id] 

                ids.append(record.chunk_id)  # same as emb_chunk_id
                docText.append(chx.text)
                vectors.append(record.vector)
                metadatas.append(
                    {
                        "page_number": chx.page_number,
                        "source": chx.source,
                        "model_used": record.model_name
                    }
                )
            else: # emb_chunk_id not in embeddings_map:
                raise ValueError(f"Missing embedding for {emb_chunk_id}")

        if ids: # safety check
            self.collection.add(
                ids=ids,
                embeddings=vectors, #cast(ChromaEmbeddings, vectors),
                documents=docText,
                metadatas=metadatas #cast(ChromaMetadatas, metadatas)
            )


    def query_vectors(self, query_embedding: List[float], top_k: int=3) -> Dict[str, Any]:
        query_list = [query_embedding]

        result = self.collection.query(
            query_embeddings=query_list,  #cast(ChromaEmbeddings, query_list),
            n_results = top_k
        )

        return result #(Dict[str, Any], result)