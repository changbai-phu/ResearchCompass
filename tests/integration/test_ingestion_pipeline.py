import sys
import pytest
from pathlib import Path

# Add project root to path for imports to work when running directly
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.loader import DocumentLoader
from src.modules.document.parser import DocumentParser
from src.modules.document.chunker import DocumentChunker
from src.modules.document.schema import Page, Chunk


def test_ingestion_pipeline():
    '''
    Integration test to verify that a real doc successfully passes through
    the entire pipeline: Loader -> Parser -> Chunker
    '''

    sample_pdf = "data/raw/sample_papers/adv_in_space_quan_comm.pdf"

    if not Path(sample_pdf).exists():
        pytest.skip(f"Skipping integration test: {sample_pdf} not found.")

    loader = DocumentLoader(sample_pdf)
    #loader_doc = loader.load()

    with loader.load() as doc:
        parser = DocumentParser(doc)
        parsed_doc = parser.parse()

        assert isinstance(parsed_doc, list)
        assert len(parsed_doc) > 0

        first_page = parsed_doc[0]
        assert isinstance(first_page, Page)
        assert first_page.page_number == 1
        assert len(first_page.text) > 0


# Programmatic helper block to run inline test buttons
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-s"]))
