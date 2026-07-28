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
def test_chuncker_success_unit():
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
    assert len(chunks_t1) == 3

    assert chunks_t1[0].text == 'abcdefghij'
    assert chunks_t1[1].text == 'ijklmnopqr'
    assert chunks_t1[2].text == 'qrstuvwxyz'

    assert chunks_t1[0].page_number == 1
    assert chunks_t1[0].source == "page_mock_1.pdf"

