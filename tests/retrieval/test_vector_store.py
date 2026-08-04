import sys
from pathlib import Path
import pytest
import shutil

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.schema import Chunk
from src.modules.retrieval.schema import Embeddings
from src.modules.retrieval.vector_store import VectorStore

# ==============================================================================
# TEST CASE 1: The Happy Path - test save_to_chroma together with query function
# ==============================================================================
def test_save_to_chroma_success_unit():
    # Arrange: mock chunk and embeddings input
    test_collection_name = "test_collection"
    chunk = Chunk(
        id="page1_0",
        text="Quantum Computation is a rapid growing field.",
        page_number=1,
        source="mock1.pdf"
    )

    emb_record = Embeddings(
        chunk_id="mock1.pdf::page1_0",
        model_name="mock-model",
        dimension=3,
        vector=[0.1, -0.2, 0.7]
    )

    store = VectorStore(collection_name=test_collection_name)

    # Act: call the function 
    store.save_to_chroma([chunk], [emb_record])
    raw_results = store.query_vectors(query_embedding=[0.1, -0.2, 0.7], top_k=1)

    # Assertion
    assert raw_results["ids"][0] == ["mock1.pdf::page1_0"]
    assert raw_results["documents"][0] == ["Quantum Computation is a rapid growing field."]
    assert raw_results["metadatas"][0][0]["source"] == "mock1.pdf"
    assert raw_results["metadatas"][0][0]["model_used"] == "mock-model"

    '''
    {
        "metadatas": [
            [
                {"page_number": 1, "source": "mock1.pdf", "model_used": "mock-model"}
            ]
        ]
    }
    '''

    # Cleanup - delete the temporary test database folder
    db_dir = Path(__file__).resolve().parents[3] / "data" / "chroma"
    if db_dir.exists():
        shutil.rmtree(db_dir)


# ==============================================================================
# TEST CASE 2: Test safety guards - empty inputs
# ==============================================================================
def test_save_to_chroma_empty_inputs_unit():
    store = VectorStore(collection_name="test_empty_collection")
    result = store.save_to_chroma(chunks=[], embeddings=[])

    assert result is None, "Check error: The function should fast-exited. "



if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-s"]))

