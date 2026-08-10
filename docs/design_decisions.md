
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