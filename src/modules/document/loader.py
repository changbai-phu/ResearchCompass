import os
import fitz # PyMuPDF fast for images or massive document
from pathlib import Path

class DocumentLoader:
    '''A modular class to handle finding and reading pdf doc'''

    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)

    def load(self) -> fitz.Document:
        if not self.file_path.exists():
            raise FileNotFoundError(f"{self.file_path} not found.")

        try:
            #with fitz.open(self.file_path) as doc:
            #    if doc.is_encrypted or len(doc) == 0:
            #        return False
            #    return True
            return fitz.open(self.file_path)
        except Exception as e:
            raise ValueError(f"Failed to read file {self.file_path}.") from e
        
'''
# Quick Test
if __name__ == "__main__":
    loader_instance = DocumentLoader("data/raw/sample_papers/adv_in_space_quan_comm.pdf")
    try:
        doc = loader_instance.load()
        print(f"Successfully loaded, the doc has {len(doc)} pages.")
    except FileNotFoundError as e:
        print(f"Path Error: {e}")
    except ValueError as e:
        print(f"Data Error: {e}")
'''