from dataclasses import dataclass

@dataclass
class Page:
    text: str
    page_number: int
    source: str #filename

@dataclass
class Chunk:
    id: str
    text: str
    page_number: int
    source: str
    # embedding:
    # metadata:
    # score

'''
@dataclass
class MetaData:
    source: str
    title: str
    authors: list[str]
    year: int
'''