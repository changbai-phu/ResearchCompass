
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
- Vectore store only for store and search acquired vectors, not deciding.
- So can later adding reranking/hybrid search/query expansion without changing storage layer. 