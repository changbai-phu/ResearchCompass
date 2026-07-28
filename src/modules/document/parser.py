import fitz
from typing import List, Dict, Any
from src.modules.document.schema import Page


class DocumentParser:
    '''A modular class to handle extracting raw text from an 
        opened pdf doc.'''

    def __init__(self, document: fitz.Document) -> None:
        #if not isinstance(document, fitz.Document):
        #    raise TypeError("DocumentParser requires a valid fitz.Document object.")
        self.doc = document

    def parse(self) -> List[Page]:
        parsed_doc: List[Page] = []

        for pnum, page in enumerate(self.doc): # it's safe to ignore the warning here, simply pylance not recognize it is fitz.Doc
            text = page.get_text().strip()
            if text:
                parsed_doc.append(
                    Page(text=text, page_number=pnum+1)
                )

        return parsed_doc

