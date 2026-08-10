import sys
import pytest
from pathlib import Path
import pytest
import shutil

# Add project root to path for imports to work when running directly
sys.path.insert(0, str(Path(__file__).parents[2])) #same as parent.parent.parent

from main import run_pipeline
from src.modules.retrieval.schema import Embeddings, RetrievedChunk



def test_ingestion_pipeline():
    '''
    Integration test to verify that a real doc successfully passes through
    the entire pipeline: Loader -> Parser -> Chunker
    '''

    sample_pdf = "data/raw/sample_papers/adv_in_space_quan_comm.pdf"

    if not Path(sample_pdf).exists():
        pytest.skip(f"Skipping integration test: {sample_pdf} not found.")

    # Act: Execute the ingestion pipeline
    retriever = run_pipeline(sample_pdf)

    # Assertion
    assert retriever is not None, "Pipeline failed: run_pipeline returns None."

    results = retriever.retrieve("Global quantum internet", top_k=2)
    assert isinstance(results, list), "Retriever must return a list."
    assert len(results) == 2, "Expected exactly top_k number of matching retrieved chunks."

    first_match = results[0]
    assert isinstance(first_match, RetrievedChunk), "Matched entry must be RetrievedChunk Dataclass."
    assert first_match.score >= 0.0, "Distance metric must be a non-negative value."
    assert first_match.chunk.source == Path(sample_pdf).name, "Source filename corrupted."
    assert first_match.chunk.page_number > 0, "Page number corrupted."
    assert len(first_match.chunk.text) > 0
    assert len(first_match.chunk.id) > 0

    # --- CLEANUP ---
    db_dir = Path(__file__).resolve().parents[3] / "data" / "chroma"
    if db_dir.exists():
        shutil.rmtree(db_dir)


# Programmatic helper block to run inline test buttons
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-s"]))
