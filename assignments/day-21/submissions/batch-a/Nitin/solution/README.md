# Day 21 - RAG Evaluation Research Prototype

## 1. Research Question

Which retrieval design gives the most reliable grounded answers for the chosen document collection, and what evidence supports the conclusion?

## 2. Document Collection

The knowledge base contains 20 short educational documents covering Python, machine learning, artificial intelligence, and Scikit-learn concepts.

The documents were written as a small classroom research dataset using information based on publicly available Python and Scikit-learn documentation.

Each document contains:

- Document ID
- Text
- Source

The source field records the documentation source used for the content.

## 3. Chunking Rules

Each document is treated as one clean chunk because the prototype uses short, self-contained educational statements.

No document is split into smaller chunks because each statement contains one main concept.

## 4. Retrieval Methods

### TF-IDF

TF-IDF represents documents using term importance and compares the query with documents using cosine similarity.

### BM25

BM25 is a lexical retrieval method that ranks documents according to query-term frequency, document length, and how informative the terms are across the collection.

## 5. Evaluation Dataset

The evaluation contains 12 questions.

Each question has a known expected document containing the answer.

The evaluation measures:

- Top-1 accuracy
- Top-3 accuracy

## 6. Experimental Results

| Retrieval Method | Top-1 Accuracy | Top-3 Accuracy |
|---|---:|---:|
| TF-IDF | 0.750 | 0.833 |
| BM25 | 0.500 | 0.667 |

TF-IDF retrieved the correct document first for 75% of the questions.

The correct document appeared in the top three results for 83.3% of the questions.

BM25 achieved 50% Top-1 accuracy and 66.7% Top-3 accuracy.

## 7. Error Analysis

Some retrieval errors occurred because short questions did not always contain the same keywords used in the documents.

TF-IDF performed better on this dataset because cosine similarity captured useful term overlap across the short educational documents.

BM25 also retrieved related documents, but some queries ranked semantically related concepts above the expected document.

The results should not be generalized to all datasets because the test collection is small and controlled.

## 8. Ablation Experiment

An ablation experiment was performed by changing the number of retrieved documents from Top-1 to Top-3.

With Top-1 retrieval, TF-IDF achieved 75.0% accuracy.

When three documents were retrieved, the correct document appeared in 83.3% of cases.

This shows that retrieving additional candidates can improve recall and give a downstream answer-generation system more relevant evidence.

## 9. Grounded Answer Generation

For a RAG system, the retrieved document should be provided to the language model as context.

Example:

Question:
What is classification?

Retrieved context:
"Classification is a supervised learning task in which a model predicts a category or class."

Grounded answer:
Classification is a supervised learning task where a model predicts a category or class.

Citation:
[Document 15 - Scikit-learn documentation]

The citation points to the retrieved document used as evidence.

## 10. Retrieval Comparison

TF-IDF was the stronger retrieval method in this experiment.

Its Top-1 accuracy was 75.0%, compared with 50.0% for BM25.

Its Top-3 accuracy was 83.3%, compared with 66.7% for BM25.

Therefore, TF-IDF provided more reliable retrieval for this particular document collection and evaluation set.

## 11. Limitations

### Hallucination Risk

A language model can generate information that is not supported by the retrieved documents.

### Missing Documents

If the knowledge base does not contain the required information, retrieval cannot provide reliable evidence.

### Weak Citations

A citation is only useful when it actually supports the generated claim.

### Evaluation Bias

The test questions and documents were created for a small controlled experiment, so the results may favor the methods used.

### Small Dataset

Only 20 documents and 12 questions were evaluated, which is too small for broad conclusions.

## 12. Final Conclusion

For this research prototype, TF-IDF produced the most reliable retrieval results.

The evidence is its higher Top-1 accuracy of 75.0% and higher Top-3 accuracy of 83.3%, compared with BM25 scores of 50.0% and 66.7%.

Therefore, TF-IDF is the preferred retrieval design for this particular knowledge base, although larger and more diverse datasets would be needed before making a general claim about retrieval systems.