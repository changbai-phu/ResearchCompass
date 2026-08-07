import sys
from pathlib import Path
from typing import Optional

# Add project root to path for imports to work when running directly
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Ingestion Modules
from src.modules.document.loader import DocumentLoader
from src.modules.document.parser import DocumentParser
from src.modules.document.chunker import DocumentChunker
#from src.modules.document.schema import Page, Chunk

# Retrieval Modules
#from src.modules.retrieval.schema import Embeddings, RetrievedChunk
from src.modules.retrieval.embedder import TextEmbedder
from src.modules.retrieval.vector_store import VectorStore
from src.modules.retrieval.retriever import TextRetriever


def run_pipeline(file_path: str) -> Optional[TextRetriever]:
    '''
    Orchestrate the ingestion pipeline:
    Loader -> Parser -> Chunker -> Embedder -> VectorStore.
    Then return a initialized TextRetriever if successful.
    '''

    print(f"[1/4] Starting pipeline for: {Path(file_path).name}")

    retriever = None
    # ==========================================================================
    # THE MAIN PIPELINE
    # ==========================================================================
    try:
        # 1. initialize the loader
        loader = DocumentLoader(file_path)

        # 2. open doc and process doc
        with loader.load() as doc:
            # parse the doc and process into Page
            parser = DocumentParser(doc)
            parsed_doc = parser.parse() # parsed_doc is Page dataclass 
            print(f"[2/4] Successfully parsed {len(parsed_doc)} pages.")

            # pass to chunker
            chunker = DocumentChunker(chunk_size=500, chunk_overlap=50)
            chunks = chunker.chunk(parsed_doc) # chunks is Chunk dataclass
            print(f"[3/4] Successfully sliced document into {len(chunks)} chunks.")

            if chunks:
                print(f"\nSample Chunk 1 (ID: {chunks[0].id}) : ")
                print(f"{chunks[0].text[:100]}...\n")

            # pass chunks to embedder 
            model_name = "all-MiniLM-L6-v2"
            embedder = TextEmbedder(model_name)
            embedded_chunks= embedder.embed_chunks(chunks) # embedded_chunks is Embeddings dataclass
            print(f"[4/4] Successfully generate {len(embedded_chunks)} embeddings.")

            # Save to the ChromaDB (local)
            collection_name="sample_collection"
            store = VectorStore(collection_name)
            store.save_to_chroma(chunks, embedded_chunks)
            print(f"Vector store successful.\n")

            # define retriever 
            retriever = TextRetriever(embedder=embedder, store=store)
            return retriever

    except FileNotFoundError as e:
        print(f"Configuration Error: {e}")
    except ValueError as e:
        print(f"Processing Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    return None


def main():
    target_file = "data/raw/sample_papers/adv_in_space_quan_comm.pdf"
    retriever = run_pipeline(target_file)
    top_k = 3

    if not retriever:
        print("Failed to launch retrieval module due to ingestion error.")
        return 

    print("Successful ingestion pipeline loaded!\n")
    print("Type your question below to query the document. Type 'exit' to quit.\n")

    while True:
        user_query = input("Enter your search query: ").strip()

        if user_query.lower() in ["exit", "quit", "q"]:
            print("Shutting down RAG retrieval interface.")
            break

        if not user_query:
            continue

        print("Searching vector database...")

        try:
            search_results = retriever.retrieve(user_query, top_k=top_k)
        except Exception as e:
            print("Search Error: {e}")
            continue

        if not search_results:
            print("No matching context found inside the database for the query.")
            continue

        print(f"\n Found {len(search_results)} semantic matches: \n")
        print("=" * 50)
        for idx, result in enumerate(search_results):
            print(f"{idx}: Source: {result.chunk.source} | Page: {result.chunk.page_number} | "
                  f" Distance Score: {result.score:.4f} \n")
            print(f"Text: \n\"{result.chunk.text}\"")
            print("-" * 50)
    

if __name__ == "__main__":
    main()