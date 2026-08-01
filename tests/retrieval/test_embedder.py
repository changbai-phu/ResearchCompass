import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.schema import Chunk
from src.modules.retrieval.embedder import TextEmbedder
from src.modules.retrieval.schema import Embeddings

# ==============================================================================
# TEST CASE 1: The Happy Path - test embed_chunks
# ==============================================================================
def test_embed_chunks_success_unit():
    # Arrange: create mock chunks
    chunk1 = Chunk(
        id="page1_0",
        text="Quantum Computation is a growing field.",
        page_number=1,
        source="mock1.pdf"
    )
    chunk2 = Chunk(
        id="page1_3",
        text="Quantum advantage requires more rigorous standardized benchmark",
        page_number=1,
        source="mock1.pdf"
    )
    chunks_list = [chunk1, chunk2]
    model_name = "all-MiniLM-L6-v2"

    # Act: pass mocked chunks to the functions
    embedder = TextEmbedder(model_name)
    embedded_result = embedder.embed_chunks(chunks_list)

    # Assertion
    assert isinstance(embedded_result, list)
    assert len(embedded_result) == 2

    result1 = embedded_result[0]
    assert isinstance(result1, Embeddings)
    assert result1.chunk_id == 'mock1.pdf::page1_0'
    assert result1.model_name == model_name
    assert result1.dimension == embedder.dimension
    assert isinstance(result1.vector, list)
    assert isinstance(result1.vector[0], float)
    assert len(result1.vector) == result1.dimension

# ==============================================================================
# TEST CASE 2: Test empty list 
# ==============================================================================
def test_embed_chunks_empty_input_unit():
    # Arrange: pass an empty list of chunks 
    empty_chunk_list = []
    model_name = "all-MiniLM-L6-v2"

    # Act
    embedder = TextEmbedder(model_name)
    embedded_result = embedder.embed_chunks(empty_chunk_list)

    # Assertion
    assert isinstance(embedded_result, list)
    assert len(embedded_result) == 0

# ==============================================================================
# TEST CASE 3: The Happy Path - test embed_query
# ==============================================================================
def test_embed_query_success_unit():
    # Arrange: test a single user query string transforms into a float list
    query_text = "What is quantum computing?"
    model_name = "all-MiniLM-L6-v2"

    # Act
    embedder = TextEmbedder(model_name)
    embedded_result = embedder.embed_query(query_text)

    # Assertion
    assert isinstance(embedded_result, list), "Query output should be a plain list"
    assert len(embedded_result) == embedder.dimension
    assert isinstance(embedded_result[0], float)


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-s"]))