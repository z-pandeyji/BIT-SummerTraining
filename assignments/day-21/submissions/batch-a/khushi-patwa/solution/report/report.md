# Research-Grade Retrieval-Augmented Generation (RAG) Evaluation

## Student

**Name:** Khushi Patwa

## Research Question

**Which retrieval design gives the most reliable grounded answers for the chosen document collection, and what evidence supports this conclusion?**

---

# 1. Introduction

This project implements a small Retrieval-Augmented Generation (RAG) prototype using a knowledge base of 20 AI-related documents. The objective is to compare two retrieval approaches:

- TF-IDF Retrieval
- Sentence Transformer Embeddings with FAISS

The system retrieves relevant document chunks for user questions and evaluates retrieval quality using Top-1 and Top-3 accuracy.

---

# 2. Document Collection

The knowledge base contains **20 documents** covering topics such as:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Neural Networks
- Transformers
- Attention Mechanism
- Large Language Models
- Retrieval-Augmented Generation
- Embeddings
- Vector Databases
- FAISS
- BM25
- TF-IDF
- Prompt Engineering
- Tokenization
- FastAPI
- REST API
- NumPy
- Pandas
- Scikit-learn

Each document includes:
- Title
- Definition
- Working Principle
- Applications
- Advantages
- Limitations
- Summary
- Source Reference

---

# 3. Chunking Strategy

Documents were split into chunks before indexing.

**Configuration**

- Chunk Size: 120 words
- Overlap: 20 words

This produced:

- Documents: **20**
- Chunks: **42**

Chunk overlap helps preserve context between consecutive chunks.

---

# 4. Retrieval Methods

## Method 1 – TF-IDF

TF-IDF represents documents using term frequency and inverse document frequency. Similarity is computed using cosine similarity.

### Advantages

- Fast
- Lightweight
- Good keyword matching

### Disadvantages

- Limited semantic understanding
- Sensitive to wording changes

---

## Method 2 – Sentence Transformer + FAISS

This method converts text into dense embeddings using the `all-MiniLM-L6-v2` model and stores vectors in a FAISS index.

Similarity search retrieves semantically related chunks.

### Advantages

- Understands semantic meaning
- Handles paraphrased queries
- Better retrieval quality

### Disadvantages

- Requires embedding model
- Higher computation than TF-IDF

---

# 5. Test Questions

A set of **12 evaluation questions** was created. Each question has an expected source document.

Examples include:

- What is Artificial Intelligence?
- Explain Deep Learning.
- What is BM25?
- What is FastAPI?
- What is Scikit-learn?

---

# 6. Evaluation Results

| Method | Top-1 Accuracy | Top-3 Accuracy |
|---------|---------------:|---------------:|
| TF-IDF | 83.33% | 100.00% |
| Sentence Transformer + FAISS | 100.00% | 100.00% |

---

# 7. Comparison

Sentence Transformer + FAISS consistently retrieved the expected document at Rank 1.

TF-IDF successfully retrieved the expected document within the top three results for all evaluation questions, but sometimes ranked another chunk first because it relies on keyword matching.

---

# 8. Error Analysis

Observed issues include:

- TF-IDF occasionally retrieved multiple chunks from the same document.
- Keyword-based retrieval was sensitive to different wording.
- Semantic retrieval produced more reliable rankings.

---

# 9. Ablation Experiment

Chunk size was selected as the experimental variable.

| Configuration | Chunk Size | Overlap |
|--------------|-----------:|--------:|
| Default | 120 | 20 |
| Smaller Chunks | 80 | 10 |

Observation:

Smaller chunks increased the number of retrieved chunks and sometimes improved precision, but larger chunks preserved more context.

The default configuration provided the best balance for this document collection.

---

# 10. Limitations

The current prototype has several limitations.

- Small knowledge base (20 documents)
- Manual evaluation dataset
- Generated answers depend entirely on retrieved chunks
- No reranking model
- No hybrid retrieval
- Limited evaluation scope

---

# 11. Research Question Answer

**Which retrieval design gives the most reliable grounded answers for the chosen document collection, and what evidence supports this conclusion?**

Based on the experimental evaluation, **Sentence Transformer embeddings combined with FAISS provided the most reliable grounded answers.** It achieved **100% Top-1 Accuracy** and **100% Top-3 Accuracy**, outperforming TF-IDF, which achieved **83.33% Top-1 Accuracy** and **100% Top-3 Accuracy**. The semantic retrieval approach better captured the meaning of user queries, making it more robust to variations in wording and improving retrieval quality.

---

# 12. Conclusion

This project successfully implemented and evaluated a small RAG system using two retrieval methods. Experimental results demonstrated that semantic retrieval using Sentence Transformer embeddings and FAISS produced more reliable grounded answers than traditional TF-IDF retrieval for the selected document collection.

The prototype satisfies the required components of a research-grade RAG evaluation, including document collection, chunking, multiple retrieval methods, evaluation metrics, error analysis, ablation study, and grounded answer generation.