## DocumentLoader
(src/modules/document/loader.py)  
- `def load(self) -> fitz.Document`

&darr;  
&darr; Document hands off to Parser.  
&darr;    

## DocumentParser
(src/modules/document/parser.py)  
- `def parse(self) -> List[Page]`

&darr;  
&darr; Loaded Document into List of Pages hands off to Chunker.  
&darr;  

## DocumentChunker
(src/modules/document/chunker.py)  
- `def chunk(self, pages: List[Page]) -> List[Chunk]`

&darr;  
&darr; Chunk Pages into chunks and hands off to Embedder.  
&darr;  

## TextEmbedder 
(src/modules/retrieval/embedder.py)  
- `embed_chunks(self, chunks: List[Chunk]) -> List[Embeddings]`  

- `embed_query(self, query_text: str) -> List[float]`  

&darr;  
&darr; Query vector hands off to Store.  
&darr;  

## (Local) VectorStore 
(src/modules/retrieval/vector_store.py)  
- `save_to_chroma(self, chunks: List[Chunk], embeddings: List[Embeddings]) -> None`  

- `query_vectors(self, query_embedding: List[float], top_k: int=3) -> Dict[str, Any]`

&darr;  
&darr; Raw Dict hands off to Retriever.   
&darr;  

## Retrieval 
(src/modules/retrieval/retriever.py)  
- `def retrieve(self, query_text: str, top_k: int=3) -> List[RetrievedChunk]`

