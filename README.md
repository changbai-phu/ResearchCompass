# ResearchCompass

AI Research Assistant & Evaluation Platform

## Problem
Researchers spend a lot of time:
* searching papers
* comparing results
* verifying AI-generated summaries
* checking citations
* organizing knowledge

Current LLMs help, but their outputs vary in quality and can hallucinate.


## Core features
1. Paper Retrieval
- Upload PDFs.

Examples:
* arXiv papers
* Nature papers
* Quantum papers
* AI papers

2. RAG
Ask questions like: Compare BB84 and MDI-QKD.

3. Multi-model comparison
- GPT/Claude/Gemini/Open-source model (optional)
- All answer the same question.

4. Evaluation
Automatically score:
* Faithfulness
* Groundedness
* Relevance
* Completeness
* Citation quality
* Hallucination risk
- using tools like DeepEval or RAGAS.


5. Human feedback
Allow users to:
👍 Helpful
👎 Not helpful
⭐ Rate the answer
- Add comments.


6. Memory
The assistant remembers:
* research interests (e.g., satellite QKD)
* preferred papers
* previous questions
* saved notes

7. Research notebook
Store:
* generated summaries
* personal notes
* extracted equations
* references
This turns the system into a lightweight research workspace rather than just a chatbot.


### Phase 2 
1. Paper Comparison
- Upload three papers. The system produces:
* comparison table
* common methods
* limitations
* datasets
* future work

2. Research Gap Finder
- Prompt:
  - “Based on these five papers, identify unresolved research questions.”

3. Knowledge Graph
- Extract:
  - Paper → Authors → Topics → Methods → Results
- Visualize relationships between concepts.

4. Citation Verification
When the model makes a claim, link it back to the supporting passage in the uploaded paper.


⸻


Initial dataset:
For example:
* BB84
* MDI-QKD
* Satellite QKD
* Quantum repeaters
* Atmospheric turbulence
* Error correction in quantum communication


Three milestones:
1. Foundation (1–2 weeks): PDF ingestion, RAG, multi-model comparison, and a clean interface.
2. Evaluation (1 week): Add automated metrics (DeepEval/RAGAS), citation grounding, and human feedback.
3. Research capabilities (1–2 weeks): Memory, paper comparison, research gap identification, and a personal research notebook.
