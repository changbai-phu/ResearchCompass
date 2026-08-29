'''
Turning user query and List[RetrievedChunk] from retriever into the LLM prompt input.
Should also provide a template for prompt.
Pass the generated prompt to generator.
'''
from typing import List
from pathlib import Path
from src.modules.retrieval.schema import RetrievedChunk
from src.modules.generation.schema import Message


class PromptBuilder:
    '''
    Handles raw text chunks and user queries into structured input for the LLM.
    '''
    def __init__(self) -> None:
        prompt_dir = Path(__file__).resolve().parent 

        try:
            self.system_instruction = (prompt_dir / "role.md").read_text(encoding="utf-8").strip()
            self.user_template = (prompt_dir / "prompts.md").read_text(encoding="utf-8").strip()
        except FileNotFoundError:
            self.system_instruction = "You are a professional research assistant."
            self.user_template = "Answer based on context. CONTEXT:\n{{context}}\n\nQUESTION: {{question}}"

    def build(self, query_text: str, retrieved_chunks: List[RetrievedChunk]) -> List[Message]:
        '''
        Insert parameters into the template placeholder slots, and compile the unified output
        '''
        context_blocks: List[str] = []

        for idx, item in enumerate(retrieved_chunks):
            block = (
                f"[Document {idx + 1}] \n"
                f"Source Filename: {item.chunk.source} \n"
                f"Page Number: Page {item.chunk.page_number} \n"
                f"Text Segment: {item.chunk.text} \n"
            )
            context_blocks.append(block)

        compiled_context_str = "\n".join(context_blocks)

        populated_user_content = self.user_template.replace(
            "{{context}}", compiled_context_str
        ).replace(
            "{{question}}", query_text
        )

        return [
            Message(
                role="system",
                content=self.system_instruction
            ),
            Message(
                role="user",
                content=populated_user_content
            )]