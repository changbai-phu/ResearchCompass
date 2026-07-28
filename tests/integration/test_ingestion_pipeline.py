import pytest
from pathlib import Path
from src.modules.document.loader import DocumentLoader
from src.modules.document.parser import DocumentParser
from src.modules.document.schema import Page

'''Using real existed paper for integration tests'''
def test_ingestion_pipeline():
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
        