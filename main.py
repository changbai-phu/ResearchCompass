import sys
from pathlib import Path

# Add project root to path for imports to work when running directly
sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.modules.document.loader import DocumentLoader
from src.modules.document.parser import DocumentParser
from src.modules.document.chunker import DocumentChunker
#from src.modules.document.schema import Page, Chunk


def run_pipeline(file_path: str) -> None:
    print(f"Starting ingestion pipeline for: {Path(file_path).name}")

    try:
        # 1. initialize the loader
        loader = DocumentLoader(file_path)

        # 2. open doc and process doc
        with loader.load() as doc:
            # parse the doc and process into Page
            parser = DocumentParser(doc)
            parsed_doc = parser.parse() # parsed_doc is Page dataclass 

            # pass to chunker
            chunker = DocumentChunker(chunk_size=500, chunk_overlap=50)
            chunks = chunker.chunk(parsed_doc) # chunks is Chunk dataclass

            if chunks:
                print(f"\nSample Chunk 1 (ID: {chunks[0].id}) : ")
                print(f"{chunks[0].text[:100]}...\n")

    except FileNotFoundError as e:
        print(f"Configuration Error: {e}")
    except ValueError as e:
        print(f"Processing Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    target_file = "data/raw/sample_papers/adv_in_space_quan_comm.pdf"
    run_pipeline(target_file)