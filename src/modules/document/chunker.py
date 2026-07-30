from typing import List
from src.modules.document.schema import Page, Chunk

class DocumentChunker:
    '''A modular class to handle chunking a pdf file into multiple chunks.'''

    def __init__(self, chunk_size: int=500, chunk_overlap: int=100):
        if chunk_size <= 0 or chunk_overlap < 0 or chunk_overlap >= chunk_size:
            raise ValueError("Check value of chunk_size and chunk_overlap.")
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, pages: List[Page]) -> List[Chunk]:
        chunks = []

        for page in pages:
            text = page.text
            start  = 0 
            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start: end]
                chunks.append(
                    Chunk(
                        id=f"page{page.page_number}_{start}",
                        page_number=page.page_number,
                        text=chunk_text,
                        source=page.source
                    )
                )
                start += (self.chunk_size - self.chunk_overlap)

        return chunks