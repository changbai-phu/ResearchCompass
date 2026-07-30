from dataclasses import dataclass
from typing import List

@dataclass
class Embeddings:  
    chunk_id: str
    model_name: str
    dimension: int
    vector: List[float]