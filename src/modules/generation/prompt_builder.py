'''
Turning user query and List[RetrievedChunk] from retriever into the LLM prompt input.
Should also provide a template for prompt.
Pass the generated prompt to generator.
'''
from typing import List, Dict
from pathlib import Path
from src.modules.retrieval.schema import RetrievedChunk


class PromptBuilder:
    '''
    Handles raw text chunks and user queries into structured input for the LLM.
    '''
    def __init__(self) -> None:
        prompt_path = Path(__file__).resolve().parent / "prompts.md"

        try:
            self.system_instruction = prompt_path.read_text(encoding="utf-8").strip()
        except FileNotFoundError:
            self.system_instruction = "You are a professional research assistant. Answer based on context."

    def prompt_build(self, query: str, context: List[RetrievedChunk]) -> str: # prompt str output
        