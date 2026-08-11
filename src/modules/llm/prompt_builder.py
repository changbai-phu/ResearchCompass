'''
Turning user query and List[RetrievedChunk] from retriever into the LLM prompt input.
Should also provide a template for prompt.
Pass the generated prompt to generator.
'''


class PromptBuilder:
    def __init__(self) -> None:


    def prompt_build(self, query: str, context: List[RetrievedChunk]) -> str: # prompt str output



        '''
        prompt_template = "
        You are a research assistant.

        Answer the question using only the provided context.
        If the context does not contain enough information, say so.

        Context:

        [Source: paper.pdf, Page 3]
        Quantum advantage refers to ...

        [Source: paper.pdf, Page 5]
        A quantum computer can ...

        Question:
        What is quantum advantage?
        "
        
        '''