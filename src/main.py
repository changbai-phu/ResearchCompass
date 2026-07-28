from src.modules.document.loader import DocumentLoader
from src.modules.document.parser import DocumentParser
from src.modules.document.schema import Page

def run_pipeline(file_path: str):
    # 1. initialize the loader
    loader = DocumentLoader(file_path)

    # 2. open doc and process doc
    with loader.load() as doc:
        #p parse the doc
        parser = DocumentParser(doc)
        parsed_doc = parser.parse()

        # pass to chucker
        # chunker = DocumentChunker()
        # chunks = chunker.chunk(parsed_doc)