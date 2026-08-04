



## TextEmbedder 
(src/modules/retrieval/embedder.py)  
`embed_chunks(self, chunks: List[Chunk]) -> List[Embeddings]`  

`embed_query(self, query_text: str) -> List[float]`  

Query vector hands off to Store.

## (Local) VectorStore 
(src/modules/retrieval/vector_store.py)
`save_to_chroma(self, chunks: List[Chunk], embeddings: List[Embeddings]) -> None`  

`query_vectors(self, query_embedding: List[float], top_k: int=3) -> Dict[str, Any]`


Raw Dict hands off to Retriever. 

## Retrieval 


