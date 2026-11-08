# Data Notes

## 1. Document Collection

This project uses a small knowledge base of 20 educational documents covering Python programming, data analysis, and machine learning fundamentals.

The document IDs are D01 to D20.

The collection includes Python variables, Python data types, lists, tuples, dictionaries, sets, conditional statements, for loops, while loops, functions, recursion, exception handling, file handling, classes, inheritance, polymorphism, NumPy arrays, Pandas DataFrames, supervised learning, and unsupervised learning.

## 2. Source Notes

The content was written as concise educational summaries based on publicly available official documentation sources.

Sources recorded in the dataset include:

- Python Official Documentation
- NumPy Documentation
- Pandas Documentation
- Scikit-learn Documentation

The dataset is stored in:

`documents/documents.csv`

Each document contains:

- document_id
- title
- source
- text

## 3. Chunking Rules

The implementation uses clean word-based chunking.

Rules:

1. Each source document is processed independently.
2. Documents are split into chunks of at most 80 words.
3. Chunks never cross document boundaries.
4. Every chunk retains the document ID, title, source, and chunk ID.
5. Chunk IDs use the format `D01_1`.

## 4. Dataset Size

The knowledge base contains 20 documents.

Because each document is short and fits within the configured 80-word chunk size, the current experiment creates 20 chunks.

Each document is represented by one chunk in the current experiment.

## 5. Evaluation Questions

The evaluation contains 12 questions.

Each question has a known expected document ID.

The questions cover variables, data types, lists, tuples, dictionaries, sets, conditional statements, for loops, while loops, functions, recursion, and exception handling.

## 6. Evaluation Design

Two retrieval methods are compared.

### BM25

BM25 is a lexical retrieval method based on term frequency and inverse document frequency. It also considers document length.

### TF-IDF

TF-IDF represents documents and queries using weighted term vectors. Cosine similarity is used to compare the query with document chunks.

## 7. Ablation Experiment

The number of retrieved chunks was varied:

- k = 1
- k = 3
- k = 5

The purpose was to test whether retrieving more candidate chunks improves evidence coverage.

## 8. Reproducibility

The experiment can be reproduced by running:

```bash
python rag_evaluation.py
```
