import sys
from pathlib import Path
import pytest
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.schema import Chunk
from src.modules.retrieval.schema import Embeddings, RetrievedChunk
from src.modules.retrieval.embedder import TextEmbedder
from src.modules.retrieval.vector_store import VectorStore
from src.modules.retrieval.retriever import TextRetriever


# ==============================================================================
# TEST CASE 1: The Happy Path - success retrieval and data reconstruction
# ==============================================================================
def test_retrieve_success_unit():
    '''
    Test that the retriever successfully coordinates the embedder and store,
    reconstruct the ChromaDB nested-list returns into RetrievedChunk dataclass.
    '''
    # Arrange: mock the embedder and store - use MagicMock for unit test to avoid dependency
    mock_embedder = MagicMock(spec=TextEmbedder)
    mock_embedder.embed_query.return_value = [0.1, 0.2, 0.3]

    mock_chroma_output = {
        "ids":[["mock_paper.pdf::page1_0"]],
        "documents":[["Quantum computing is a rapid growing field."]],
        "metadatas":[[
            {
                "page_number": 1,
                "source": "mock_paper.pdf",
                "model_used": "mock_model"
                }
        ]],
        "distances":[[0.1234]]
    }

    mock_store = MagicMock(spec=VectorStore)
    mock_store.query_vectors.return_value = mock_chroma_output

    retriever = TextRetriever(embedder=mock_embedder, store=mock_store)

    # Act
    results = retriever.retrieve(query_text="quantum computing field", top_k=1)

    # Assertion
    assert isinstance(results, list)
    assert len(results) == 1

    assert isinstance(results[0], RetrievedChunk)
    assert results[0].score == 0.1234

    assert results[0].chunk.id == "page1_0", "Compound chunk ID prefix failed to restore original chunk ID."
    assert results[0].chunk.source == "mock_paper.pdf"
    assert results[0].chunk.page_number == 1
    assert "Quantum computing" in results[0].chunk.text


# ==============================================================================
# TEST CASE 2: Empty database
# ==============================================================================
def test_retriever_empty_database_unit():
    '''
    Test if Chroma returns its standard blank dictionary result, which the retriever
    should catch it immediately and fast exit.
    '''
    # Arrange: mock 
    mock_embedder = MagicMock(spec=TextEmbedder)
    mock_embedder.embed_query.return_value = [0.1, 0.2, 0.3]

    mock_chroma_output = {
        "ids":[[]],
        "documents":[[]],
        "metadatas":[[]],
        "distances":[[]]
    }

    mock_store = MagicMock(spec=VectorStore)
    mock_store.query_vectors.return_value = mock_chroma_output

    retriever = TextRetriever(embedder=mock_embedder, store=mock_store)

    # Act
    results = retriever.retrieve(query_text="mock empty query", top_k=1)

    # Assert
    assert isinstance(results, list)
    assert len(results) == 0, "Safety guard failed to fast exit when database is empty"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-s"]))