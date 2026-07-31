'''
A transformer that takes text(chunks or user queries)  -> vector
'''
from typing import List
from sentence_transformers import SentenceTransformer
from src.modules.document.schema import Chunk
from src.modules.retrieval.schema import Embeddings


class DocumentEmbedder:
    '''
    Processes raw document text chunks into Embeddings records.
    Chunks -> SentenceTransformer -> Embeddings
    '''
    def __init__(self, model_name: str="all-MiniLM-L6-v2") -> None:
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()

    def embed_chunk(self, chunks: List[Chunk]) -> List[Embeddings]:
        '''
        Read a list of upstream Chunks, calculate vectors, and generate embeddings
        '''
        compiled_embeddings: List[Embeddings] = []

        texts_to_embed = [ch.text for ch in chunks]
        raw_vectors = self.model.encode(texts_to_embed).tolist()  #normalize_embeddings=True

        for idx, chunk in enumerate(chunks):
            unique_chunk_id = f"{chunk.source}_{chunk.id}"

            compiled_embeddings.append(
                Embeddings(
                    chunk_id = unique_chunk_id,
                    model_name = self.model_name,
                    dimension = self.dimension,
                    vector = raw_vectors[idx]
                )
            )

        return compiled_embeddings


    def embed_query(self, query_text: str) -> List[float]:
        '''
        Converts a user's question into a raw vector for database searching.
        '''
        # encode() returns a numpy array, convert it to a standard list of floats
        return self.model.encode(query_text).tolist()