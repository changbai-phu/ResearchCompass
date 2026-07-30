import sys
from pathlib import Path
import pytest
import fitz

# Add project root to path for imports to work when running directly
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.chunker import DocumentChunker
from src.modules.document.schema import Page, Chunk

'''
Core logic shall be tested:
- Split text into chunks of the required size
- Preserve the overlap between consecutive chunks
- Preserve metadat (page_number, source)
- Generate proper unique chunk.id
'''

# ==============================================================================
# TEST CASE 1: The Happy Path (Verify chunking, overlap and metadata)
# ==============================================================================
def test_chunker_success_unit():
    page_mock_1 = Page(
        text="abcdefghijklmnopqrstuvwxyz",
        page_number=1,
        source="page_mock_1.pdf"
    )
    chunker_test_1 = DocumentChunker(
        chunk_size=10,
        chunk_overlap=2
    )
    chunks_t1 = chunker_test_1.chunk([page_mock_1])

    assert isinstance(chunks_t1, list)
    assert len(chunks_t1) == 4
    # test chunking and overlap
    assert chunks_t1[0].text == 'abcdefghij'
    assert chunks_t1[1].text == 'ijklmnopqr'
    assert chunks_t1[2].text == 'qrstuvwxyz'
    assert chunks_t1[3].text == 'yz'
    # test other attributes
    assert chunks_t1[0].page_number == 1
    assert chunks_t1[0].source == "page_mock_1.pdf"
    # test id
    assert chunks_t1[0].id == 'page1_0'
    assert chunks_t1[1].id == 'page1_8'
    assert chunks_t1[2].id == 'page1_16'

def test_chunker_empty_pages_unit():
    chunker_test_2 = DocumentChunker()
    chunks_t2 = chunker_test_2.chunk([])
    assert chunks_t2 == []

def test_chunker_invalid_chunk_value_unit():
    with pytest.raises(ValueError):
        DocumentChunker(
            chunk_size = 10,
            chunk_overlap = 10
        )

    
# Programmatic helper block to run inline test buttons
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))

'''
or run below command in terminal
python -m pytest tests/document/test_loader.py -v
'''