import pytest
from src.modules.document.loader import DocumentLoader

'''Using real existed paper for integration tests'''
def test_ingestion_pipeline():
    sample_pdf = "data/raw/sample_papers/adv_in_space_quan_comm.pdf"
    loader = DocumentLoader(sample_pdf)
    loader_doc = loader.load()