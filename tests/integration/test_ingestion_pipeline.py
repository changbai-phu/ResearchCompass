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

    # Act: Execute the ingestion pipeline
    loader = DocumentLoader(sample_pdf)

    with loader.load() as doc:
        parser = DocumentParser(doc)
        parsed_doc = parser.parse()

        chunker = DocumentChunker(chunk_size=500, chunk_overlap=50)
        chunks = chunker.chunk(parsed_doc)

        # Assertion
        assert isinstance(chunks, list)
        assert len(chunks) > 0

        chunk_1 = chunks[0]
        assert isinstance(chunk_1, Chunk)
        assert "page1" in chunk_1.id
        assert chunk_1.page_number == 1
        assert len(chunk_1.text) > 0
        assert chunk_1.source == Path(sample_pdf).name


# Programmatic helper block to run inline test buttons
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-s"]))
