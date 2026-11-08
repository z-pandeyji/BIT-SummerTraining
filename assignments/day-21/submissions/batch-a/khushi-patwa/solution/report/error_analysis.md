# Error Analysis

During evaluation, TF-IDF achieved 83.33% Top-1 Accuracy while Sentence Transformer + FAISS achieved 100% Top-1 Accuracy.

## Observations

- TF-IDF sometimes returned multiple chunks from the same document.
- TF-IDF relies on exact keyword matching.
- When different wording or synonyms were used, TF-IDF occasionally ranked another chunk first.
- Embedding retrieval understood semantic meaning and consistently returned the expected document.

## Example

Question:

What is Artificial Intelligence?

TF-IDF returned two chunks from the AI document before retrieving other related concepts.

Embedding retrieval directly identified the correct document because semantic similarity was preserved.