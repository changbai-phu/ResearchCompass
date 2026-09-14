'''
Call LLM API with the prompt (from prompt_builder).
Will use Qwen or Deepseek first, later change to OpenAI for comparison. 
'''
import os
from typing import List, Optional, cast
from openai import OpenAI

from src.modules.generation.schema import Message, LLMResponse
from src.modules.retrieval.schema import RetrievedChunk


class LLMGenerator:
    def __init__(self, provider: str="deepseek", model_name: Optional[str]=None) -> None:
        self.provider = provider.lower()

        if self.provider == "deepseek":
            self.model_name = model_name or "deepseek-chat"
            self.client = OpenAI(
                api_key = os.environ.get("DEEPSEEK_API_KEY", "mock_key"),
                base_url = "https://deepseek.com"
            )
        elif self.provider == "qwen":
            self.model_name = model_name or "qwen-max"
            self.client = OpenAI(
                api_key = os.environ.get("QWEN_API_KEY", "mock_key"),
                base_url = "https://aliyuncs.com"
            )
        elif self.provider == "openai":
            self.model_name = model_name or "gpt-4o-mini"
            self.client = OpenAI(
                api_key = os.environ.get("OPENAI_API_KEY", "mock_key"),
                base_url = " ? "
            )
        else:
            raise ValueError(f"Unknown LLM provider specified: '{provider}'")

        def generate(self, prompt: str) -> str: