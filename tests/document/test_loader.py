import pytest
from src.modules.document.loader import DocumentLoader

def test_loader():
    loader = DocumentLoader("data/raw/sample_papers/adv_in_space_quan_comm.pdf")
    loader_doc = loader.load()

    assert len(loader_doc) > 0
