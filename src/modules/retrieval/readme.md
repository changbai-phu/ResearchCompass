## Future Improvements

### Embedding Evaluation
Currently using: sentence-transformers/all-MiniLM-L6-v2

Future experiments:
- Compare BGE-M3
- Compare OpenAI text-embedding models
- Build retrieval benchmark dataset
- Evaluate Recall@k and MRR
  
Models:
- BGE: bge-large-en-v1.5 or bge-m3 (base:768, large:1024)
- E5: e5-large-v2 or multilingual-e5-large (?)
- SentenceTransformer: all-MiniLM-L6-v2 (384)
- OpenAI embedding: text-embedding-3-small or text-embedding-3-large (small:1536, large:30072)


### LangChain Comparison
Future experiments:
- using LC to replace some of current functions (?) 