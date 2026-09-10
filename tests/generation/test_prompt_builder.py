import sys
from pathlib import Path
import pytest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.schema import Chunk
from src.modules.retrieval.schema import RetrievedChunk
from src.modules.generation.schema import Message
from src.modules.generation.prompt_builder import PromptBuilder

# ==============================================================================
# TEST CASE 1: The Happy Path
# Test that promptBuilder successfully parses a markdown prompt template,
# replace {{context}}, {{question}} placeholder in user_template,
# and returns structured Message dataclass.
# ==============================================================================
def test_prompt_build_success_unit(tmp_path):
    # Arrange
    mock_role_content = "You are an specialist in quantum computing."
    mock_prompt_content = "Answer based on context. CONTEXT:\n{{context}}\n\nQUESTION: {{question}}."

    role_file = tmp_path / "role.md"
    prompts_file = tmp_path / "prompts.md"

    role_file.write_text(mock_role_content, encoding='utf-8')
    prompts_file.write_text(mock_prompt_content, encoding='utf-8')

    # intercept the parent lookup line inside the file package setup
    with patch("src.modules.generation.prompt_builder.Path") as mock_path:
        mock_path.return_value.resolve.return_value.parent = tmp_path
        builder = PromptBuilder()

    chunk = Chunk(
        id="page1_0",
        text="Quantum Computation is a growing field. It includes several growing fields.",
        page_number=1,
        source="mock1.pdf"
    )
    retrieved_chunk = RetrievedChunk(
        chunk=chunk,
        score=0.02
    )

    # Act
    messages = builder.build(
        query_text="What is quantum computing?",
        retrieved_chunks=[retrieved_chunk]
    )

    # Assert
    assert isinstance(messages, list) # verify structured output
    assert len(messages) == 2

    assert messages[0].role == "system"
    assert messages[0].content == mock_role_content

    assert messages[1].role == "user"
    assert "{{context}}" not in messages[1].content
    assert "mock1.pdf" in messages[1].content
    assert "What is quantum computing?" in messages[1].content # replace the {{question}}


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "-s"]))