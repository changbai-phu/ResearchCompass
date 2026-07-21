# ResearchCompass
A modular AI-assisted research workflow for scientific literature retrieval, evaluation, and knowledge management.

## Table of Contents
- [ResearchCompass](#researchcompass)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Motivation](#motivation)
  - [Goals](#goals)
  - [Architecture](#architecture)
  - [Modular Components](#modular-components)
  - [Tech Stack](#tech-stack)
  - [Development Roadmap](#development-roadmap)
    - [Milestone 1 - Core](#milestone-1---core)
    - [Milestone 2 - Evaluation](#milestone-2---evaluation)
    - [Milestone 3 - Research Workspace](#milestone-3---research-workspace)
    - [Milestone 4 - Research Intelligence](#milestone-4---research-intelligence)
  - [Initial Research Domain](#initial-research-domain)
    - [Version 1.0 focuses on:](#version-10-focuses-on)
  - [Future Extensions](#future-extensions)


## Overview
ResearchCompass is a modular AI-assisted scientific research workflow designed to help researchers efficiently explore, analyze, and organize academic literature.

The project combines literature retrieval, Retrieval-Augmented Generation (RAG), AI response evaluation, and knowledge management into a unified research workflow. Instead of treating Large Language Models as standalone answer generators, ResearchCompass focuses on building reliable AI-assisted research processes through modular components, source-grounded responses, and continuous evaluation.

The first version of ResearchCompass focuses on quantum computing and quantum communication literature, including topics such as quantum key distribution (QKD), quantum error correction (QEC), and quantum networking. The architecture is designed to be extensible to other scientific domains by replacing or expanding domain-specific knowledge sources.

The long-term goal is to explore how AI systems can assist researchers by reducing information overload, improving literature understanding, and supporting knowledge discovery while maintaining transparency and reliability.

## Motivation
As I continue self-learning quantum computing, structured learning resources such as IBM Quantum Learning provide a strong foundation, but deeper exploration of research topics, such as surface codes in quantum error correction, parameter optimization in quantum key distribution, and emerging quantum communication technologies, requires engaging with scientific literature.

Research papers are one of the most valuable resources for understanding technical details, following new developments, and building connections between different concepts. However, navigating the rapidly growing volume of quantum computing research is challenging. Thousands of new papers are published every year, while foundational papers from earlier work remain essential for building strong understanding.

At the same time, although Large Language Models can accelerate literature exploration, they introduce challenges such as hallucinated information, unsupported claims, and inconsistent reasoning.

ResearchCompass aims to address this challenge by building a modular AI-assisted scientific research workflow that combines literature retrieval, retrieval-augmented generation (RAG), response evaluation, and knowledge organization to support more reliable and efficient research exploration.


## Goals
1. Reliable literature retrieval
   - Provide accurate answers grounded in the research papers rather than relying on model knowledge.
2. Transparent AI response
   - Generated responses should be traceable to supporting contexts from source documents. 
3. Modular AI Architecture
   - Reusable Ai components that can be extended or modified easily based on needs.
4. Improve research productivity
   - Reduce manual time of searching papers, comparing methods, organizing notes.

## Architecture
(to add)

## Modular Components
1. Document Module
2. Retrieval Module
3. LLM Module
4. Evaluation Module
5. Memory Module
6. Research Notebook
7. Research Intelligence Module

## Tech Stack
- Backend: Python
- AI: LangChain, OpenAI API/Antropic API
- Retrieval: ChromaDB/FAISS
- Embeddings: 
- Evaluation: RAGAS, DeepEval
- Database: PostgreSQL/SQLite
- Frontend: Streamlit

## Development Roadmap
### Milestone 1 - Core 
- pdf ingestion
- document parsing
- vector database
- RAG assistant
- semantic retrieval
  
### Milestone 2 - Evaluation
- automated evaluation
- citation grounding
- hallucination detection
- human feedback

### Milestone 3 - Research Workspace
- memory check 
- paper collections 
- tbd

### Milestone 4 - Research Intelligence
- paper comparison
- research gap analysis
- knowledge graph
- paper recommendation 
- tbd


## Initial Research Domain
### Version 1.0 focuses on: 
- QKD
- QEC
- Satellite Quantum Communication
- Quantum Networks
- Quantum Repeaters

## Future Extensions
- Multi-agent research workflows (may add this to current Modules)
- Experiment planning assistance
- Personalized recommendation 
- etc