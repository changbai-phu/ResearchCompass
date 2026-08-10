from dataclasses import dataclass
from typing import List

from src.modules.document.schema import Chunk

@dataclass
class Embeddings:  
    chunk_id: str
    model_name: str
    dimension: int
    vector: List[float]

@dataclass
class RetrievedChunk:
    chunk: Chunk
    score: float