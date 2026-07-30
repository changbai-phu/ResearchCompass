'''
A transformer that takes text(chunks or user queries)  -> vector
'''
from typing import List
from sentence_transformers import SentenceTransformer
from src.modules.retrieval.schema import Embeddings

