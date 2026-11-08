# Limitations

Although the RAG prototype performed well, several limitations remain.

- The knowledge base contains only 20 documents.
- Generated answers are limited to retrieved document content.
- Missing documents may lead to incomplete answers.
- Retrieval quality depends on chunk size and chunk overlap.
- Weak retrieval can still result in grounded but incomplete answers.
- Evaluation uses only 12 manually created questions, which may introduce evaluation bias.
- Larger and more diverse datasets are required for comprehensive benchmarking.

Future work could include hybrid retrieval, reranking models, and larger benchmark datasets.