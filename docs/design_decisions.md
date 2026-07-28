
## Using dataclass Page instead of Dictionary
- Originally using dictionary(Dict[str, Any])as data type for parsing document in parser.py.
  Now going to use Page from dataclasses to replace dictionary for ease use.
- Old dictionary: page_dict[i]["text"] and page_dict[i]["page_numer"]
- Page dataclass: page.text and page.page_number (is more clear notation) 
- And plus, Page is more flexible for long term extension in case of adding 
  new metadata, like filename, links, etc. 