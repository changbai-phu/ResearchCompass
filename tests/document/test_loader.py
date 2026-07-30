import sys
from pathlib import Path
import pytest
import fitz
from unittest.mock import patch, MagicMock

# Add project root to path for imports to work when running directly
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.loader import DocumentLoader

'''Using mocking library to simulate different scenarios'''
# ==============================================================================
# TEST CASE 1: The Happy Path (File exists and loads successfully)
# ==============================================================================
@patch('src.modules.document.loader.Path.exists')
@patch('src.modules.document.loader.fitz.open')
def test_loader_success_unit(mock_fitz_open, mock_exists):
    """
    Arrange: Simulate that the target PDF file exists on disk 
             and that fitz can open it as a 5-page document.
    """
    # Set up mocks
    mock_exists.return_value = True # Simulate the file exists

    mock_doc = MagicMock(spec=fitz.Document)
    mock_doc.__len__.return_value = 5 # Document has 5 pages
    mock_fitz_open.return_value = mock_doc

    # Run own code
    sample_pdf = "data/raw/sample_papers/adv_in_space_quan_comm.pdf"
    loader = DocumentLoader(sample_pdf)
    result = loader.load() # Act - execute the actual method (under test)

    # Assertions - Verify behaviors and results
    mock_fitz_open.assert_called_once_with(loader.file_path)
    assert isinstance(result, fitz.Document)
    assert len(result) == 5

# ==============================================================================
# TEST CASE 2: Error Path - Missing File
# ==============================================================================
@patch('src.modules.document.loader.Path.exists')
def test_loader_missing_file_unit(mock_exists):
    '''
    Arrange: Simulate that the file does not exist.
    '''
    mock_exists.return_value = False

    sample_pdf = "data/raw/sample_papers/missing_file.pdf"
    loader = DocumentLoader(sample_pdf)

    '''
    Act and Assert
    '''
    with pytest.raises(FileNotFoundError) as exc_info: 
        loader.load()
    assert "not found" in str(exc_info.value)

# ==============================================================================
# TEST CASE 3: Error Path - Corrupted File
# ==============================================================================
@patch('src.modules.document.loader.Path.exists')
@patch('src.modules.document.loader.fitz.open')
def test_load_corrupted_file_unit(mock_fitz_open, mock_exists):
    """
    Arrange: Simulate that the file exists, 
             but the pdf file is broken or corrupted.
    """
    mock_exists.return_value = True
    mock_fitz_open.side_effect = RuntimeError("Invalid PDF structure")

    sample_pdf = "data/raw/sample_papers/corrupted_file.pdf"
    loader = DocumentLoader(sample_pdf)

    # Act & Assert: Verify that it catches the crash 
    with pytest.raises(ValueError) as exc_info:
        loader.load()
        
    assert f"Failed to read file {loader.file_path}" in str(exc_info.value)


# Standard programmatic execution helper
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))

'''
or run below command in terminal
python -m pytest tests/document/test_loader.py -v
'''