# Retrieval Method Comparison

| Feature | TF-IDF | Sentence Transformer + FAISS |
|---------|--------|------------------------------|
| Retrieval Type | Keyword-based | Semantic-based |
| Top-1 Accuracy | 83.33% | 100.00% |
| Top-3 Accuracy | 100.00% | 100.00% |
| Speed | Very Fast | Fast |
| Semantic Understanding | No | Yes |
| Handles Synonyms | Limited | Yes |
| Best Use Case | Exact keyword search | Semantic document retrieval |

## Conclusion

Sentence Transformer with FAISS performed better than TF-IDF for this document collection. It achieved perfect Top-1 and Top-3 accuracy because it understands semantic similarity instead of relying only on keyword matching.