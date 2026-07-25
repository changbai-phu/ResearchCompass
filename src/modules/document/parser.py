import fitz
from typing import List, Dict, Any

class DocumentParser:
    '''A modular class to handle extracting raw text from an 
        opened pdf doc.'''

    def __init__(self, document: fitz.Document) -> None:
        #if not isinstance(document, fitz.Document):
        #    raise TypeError("DocumentParser requires a valid fitz.Document object.")
        self.doc = document

    def parse(self) -> List[Dict[str, Any]]:
        parsed_doc: List[Dict[str, Any]] = []

        for pnum, page in enumerate(self.doc): 
            text = page.get_text().strip()
            if text:
                parsed_doc.append(
                    {
                       "page_number": pnum + 1,
                       "text": text
                    })

        return parsed_doc

