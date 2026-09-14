from dataclasses import dataclass
from typing import List

@dataclass
class Message:      # a single structured chat message payload object
    role: str       # e.g, system or user
    content: str    # actual textual message body content

@dataclass
class LLMResponse:
    answer: str
    sources: List[str]