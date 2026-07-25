import sys
from pathlib import Path
import pytest
import fitz
from unittest.mock import patch, MagicMock

# Add project root to path for imports to work when running directly
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.parser import DocumentParser

# ==============================================================================
# TEST CASE 1: The Happy Path (Success extract)
# ==============================================================================
def test_parser_success():
    sample_pdf = Path("data/raw/sample_papers/adv_in_space_quan_comm.pdf")

    with fitz.open(sample_pdf) as doc:
        parser = DocumentParser(doc)
        result = parser.parse()

    assert isinstance(result, list)
    assert len(result) > 0

    for i, page in enumerate(result, start=1):
        assert isinstance(page, dict)

        #page_1 = result[0]
        assert "page_number" in page  #assert "page_number" in page_1
        assert "text" in page #assert "text" in page_1

        assert page["page_number"] == i
        assert isinstance(page["text"], str)
        assert len(page["text"]) > 0
        assert page["text"] == page["text"].strip() # test .strip() works

# ==============================================================================
# TEST CASE 2: Empty page
# ==============================================================================

''' Mock pages 
def test_parser_success():

    # Arrange: simulate fitz open behaviors, add trailing spaces to test .strip()

    mock_page_1 = MagicMock()
    mock_page_1.get_text.return_value = "  Quantum Computing Overview\n"

    mock_page_2 = MagicMock()
    mock_page_2.get_text.return_value = "Quantum Error Mitigations.\t"

    mock_doc = MagicMock(spec=fitz.Document)
    pages_list = [mock_page_1, mock_page_2]
    mock_doc.pages.return_value = pages_list
    mock_doc.__iter__.return_value = iter(pages_list) # prevent endless loop 
    mock_doc.__len__.return_value = len(pages_list)

   
    # Act: Run parser logic
   
    parser = DocumentParser(mock_doc)
    result = parser.parse()

  
    # Assert: verify the output list structure, and text contents
   
    assert isinstance(result, list)
    assert len(result) == 2

    assert result[0]["page_number"] == 1
    assert result[0]["text"] == "Quantum Computing Overview"

    assert result[1]["page_number"] == 2
    assert result[1]["text"] == "Quantum Error Mitigations."

'''



# Programmatic helper block to run inline test buttons
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))

'''
or run below command in terminal
python -m pytest tests/document/test_loader.py -v
'''