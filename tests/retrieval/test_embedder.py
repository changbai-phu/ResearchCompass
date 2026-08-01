import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.document.schema import Chunk
from src.modules.retrieval.embedder import TextEmbedder
from src.modules.retrieval.schema import Embeddings


def test_embed_chunks_success_unit():
    