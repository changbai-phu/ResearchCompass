
## Using dataclass Page instead of Dictionary
- Originally using dictionary(Dict[str, Any])as data type for parsing document in parser.py.
  Now going to use Page from dataclasses to replace dictionary for ease use.
- Old dictionary: page_dict[i]["text"] and page_dict[i]["page_numer"]
- Page dataclass: page.text and page.page_number (is more clear notation) 
- And plus, Page is more flexible for long term extension in case of adding 
  new metadata, like filename, links, etc. 

## Keep the tiny 'duplicated' tail of chunking 
- For the chunking function, in the case of the last chunk is 'replicated' of the last few characters of the previous chunk due to overlap size and it is near the end of the input text, instead of deleting that chunk, it is kept on purpose to avoid information loss. 

## Separate retriever from vector store
- Retriever specifically for retrieval strategy, preparing for downstream AI generation. 
- Vector store only for store and search acquired vectors, not deciding.
- So can later adding reranking/hybrid search/query expansion without changing storage layer. 

## Avoid LangChain initially
- Later may integrate with LangChain, but for now will build the pieces one by one first, can better understand what LangChain is abstracting. 

## Create new dataclass for Embedding instead of feeding to ChromaDB directly
- It seems Chroma calls embedding functions internally which is really convenient, however, for better deciding which sentence embedding technique to be used, a customized dataclass will be created. 

## Retrieval quality regarding semantic retrieval pipeline (v0.1.0)
- Does not perform well with chunk_size/chunk_overlap value 500/50, and model "all-MiniLM-L6-v2" due to different possible reasons:
  - not proper chunk size (maybe try other combinations like 300/50, 400/50 etc)
  - current small general-purpose model (will compare with different models)
  - small database, currently only have one paper 
  - no reranking (add cross-encoder reranker)
- *Note*: improvement will make for later version of Tag. 

## LLM API choices in initial generator code
- Choose Qwen/Deepseek initially because of following:
  - to make code provider independence
  - can later do model behavior comparison easier (groundedness/completeness/hallucination/cost)
  - use relatively inexpensive providers while developing and debugging, then test stronger models later.
  - considering geographic availability, payment options, model families etc.
  - for experimental purpose in evaluation module later on, e.g., does the same retrieved context + the same prompt have the similar performance across modules. 

| Provider | Model | Input / 1M tokens | Output / 1M tokens | Context | Range|
|---|---|---:|---:|---:|---:|
| Qwen | Qwen3.5-Flash | $0.115/$0.172 | $1.147/$1.72 | Up to 1M | 128K<Token≤256K |
| Qwen | Qwen3.5-Plus | $0.287/0.573 | $1.147/$3.44| Up to 1M | 128K<Token≤256K |
| DeepSeek | DeepSeek-V4-Flash | $0.14 | $0.28 | 1M | N/A |
| DeepSeek | DeepSeek-V4-Pro(no thinking) | $0.435 | $0.87| 1M | N/A |
| OpenAI | GPT-5.4 mini | $0.75 | $4.50 | 400K | N/A |
| OpenAI | GPT-5.6 Terra | $2.00 | $12 | 1M | N/A |
| OpenAI | GPT-5.6-sol | $5.00 | $30.00 | 1M | N/A |


- links for pricing:
  - [Qwen] (https://www.alibabacloud.com/help/en/model-studio/model-pricing?utm_source=chatgpt.com)
  - [DeepSeek] (https://api-docs.deepseek.com/quick_start/pricing/?utm_source=chatgpt.com)
  - [OpenAI] (https://developers.openai.com/api/docs/models)
- Links for LLM benchmark:
  - [Which LLM to Choose in 2026? Selection Guide + Benchmarks](https://iternal.ai/llm-selection-guide)
    - based on intended use-case tier:
      1. The Budget/Flash Tier (Ultra-fast, structured tasks) - classification, keyword extraction, routing queries, basic summaries.
         1. gpt-4o-mini/gpt-5.4-nano
         2. deepseek-v4-flash
         3. qwen3.5-flash
      2. The Balanced/Value Tier (Standard RAG sweet spot) - standard RAG applications, multi-page synthesis, general chatting.
         1. gpt-5.4-terra/gpt-4o
         2. deepseek-v4-pro
         3. qwen3.5-plus/qwen2.5-72b
      3. The Flagship/Reasoning Tier (Complex math, coding, logic) - heavy coding, debugging, strict mathematical reasoning, multi-step agents. 
         1. gpt-5.6-sol
         2. deepseek-v4-pro(with thinking)
         3. qwen3.8-max