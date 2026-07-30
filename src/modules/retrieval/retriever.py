'''
(retrieval strategy)
Responsible for deciding how to retrieve useful context for downstream AI tasks.
It asks the embedder for a vector, decide what to query for, map the output 
from vector_store to SearchResult dataclass. 
Future: reranking or hybrid search 
'''