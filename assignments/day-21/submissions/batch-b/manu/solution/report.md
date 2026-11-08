# RAG Retrieval Evaluation Report



## Research Question



Which retrieval design gives the most reliable grounded answers for the chosen document collection, and what evidence supports the conclusion?



## 1. Objective



This project evaluates a small Retrieval-Augmented Generation (RAG) prototype over a knowledge base of 20 educational documents.



The objective is to compare two retrieval methods:



1\. BM25

2\. TF-IDF with cosine similarity



The system retrieves relevant document chunks for user questions and produces grounded answer drafts with citations to the retrieved chunks.



## 2. Knowledge Base



The collection contains 20 documents covering Python programming, data analysis, and machine learning fundamentals.



The documents are identified as D01 to D20.



The evaluation uses 12 questions whose answers are present in the document collection.



## 3. Retrieval Methods



### BM25



BM25 is a lexical retrieval method. It ranks documents based on query term frequency, inverse document frequency, and document length normalization.



### TF-IDF



TF-IDF represents documents and queries using weighted term vectors. Cosine similarity is used to rank documents according to their similarity to the query.



## 4. Evaluation Metrics



### Top-1 Accuracy



Top-1 accuracy measures whether the correct document is ranked first.



### Top-3 Accuracy



Top-3 accuracy measures whether the correct document appears anywhere in the first three retrieved results.



## 5. Main Results



| Retrieval Method | Top-1 Accuracy | Top-3 Accuracy |

| ---------------- | -------------: | -------------: |

| BM25             |         83.33% |         91.67% |

| TF-IDF           |         75.00% |        100.00% |



## 6. Comparison



BM25 achieved the higher Top-1 accuracy of 83.33%. This means BM25 was better at placing the correct document as the single highest-ranked result.



TF-IDF achieved the higher Top-3 accuracy of 100.00%. This means that TF-IDF successfully included the correct document within the first three retrieved results for all 12 evaluation questions.



For grounded answer generation, Top-3 coverage is important because the correct evidence needs to be available in the retrieved context. Therefore, TF-IDF provided better evidence coverage in this experiment.



However, BM25 was better at first-result precision.



## 7. Error Analysis



### BM25 Errors



For the question about Python data types, BM25 ranked D03 first instead of D02. However, the correct document D02 was present within the top three results.



For the question about Python functions, BM25 retrieved D13, D11, and D02. The correct document D10 was not retrieved within the top three results.



The function question was the most significant BM25 failure because the correct evidence was completely absent from the top-three context.



### TF-IDF Errors



For the question about Python data types, TF-IDF ranked D03 first, but the correct D02 document appeared in the second position.



For the question about for loops, TF-IDF ranked D09 first, while the correct D08 document appeared in the second position.



For the question about Python functions, TF-IDF ranked D11 and D01 before the correct D10 document. The correct document was still included at rank three.



These errors show that lexical overlap between related programming concepts can cause ranking confusion.



## 8. Ablation Experiment



The number of retrieved chunks was varied using k = 1, k = 3, and k = 5.



| k | BM25 Top-1 | BM25 Top-3 | TF-IDF Top-1 | TF-IDF Top-3 |

| - | ---------: | ---------: | -----------: | -----------: |

| 1 |     83.33% |     83.33% |       75.00% |       75.00% |

| 3 |     83.33% |     91.67% |       75.00% |      100.00% |

| 5 |     83.33% |     91.67% |       75.00% |      100.00% |



Increasing the retrieval window from k=1 to k=3 improved evidence coverage for both methods.



For TF-IDF, Top-3 accuracy increased from 75.00% to 100.00%.



Increasing k from 3 to 5 did not provide additional improvement in this dataset.



This suggests that k=3 was sufficient for the current knowledge base.



## 9. Grounded Answer Generation



The prototype generates answer drafts using the highest-ranked retrieved chunk.



Each answer includes:



\* the retrieved text;

\* the chunk identifier;

\* the source name.



For example:



`\[Citation: D01\_1; Source: Python Official Documentation]`



This allows the answer to be traced back to the retrieved evidence.



However, the current prototype is a retrieval-and-answer-drafting system rather than a full large language model generation system.



## 10. Retrieval Design Comparison



| Criterion                   | BM25                 | TF-IDF                       |

| --------------------------- | -------------------- | ---------------------------- |

| Top-1 ranking               | Better               | Lower                        |

| Top-3 evidence coverage     | Lower                | Better                       |

| Exact keyword matching      | Strong               | Strong                       |

| Broad candidate coverage    | Good                 | Excellent in this experiment |

| Best use in this experiment | Precise first result | Grounded evidence retrieval  |



## 11. Most Reliable Design



Based on the experimental results, TF-IDF with k=3 provides the most reliable retrieval design for grounded answers in this document collection.



The main evidence is its 100.00% Top-3 accuracy compared with 91.67% for BM25.



Although BM25 achieved a higher Top-1 accuracy of 83.33%, TF-IDF provided complete coverage of the correct document within the top three results.



Therefore, when the primary goal is reliable grounded answer generation, TF-IDF with a retrieval window of three chunks is the strongest design among the tested configurations.



## 12. Limitations



### Hallucination Risk



The current system does not use a full generative language model. A future RAG system could still hallucinate if the generator adds information not supported by retrieved evidence.



### Missing Documents



If the knowledge base does not contain the answer, the retriever cannot retrieve the correct evidence.



### Weak Citations



The current citations identify the retrieved chunk and source name. They do not yet provide full URLs, page numbers, or paragraph-level citations.



### Evaluation Bias



The evaluation questions were created from the same document collection. This may make the questions easier than real-world user questions.



### Small Dataset



The experiment uses only 20 short documents and 12 evaluation questions. Results may change on a larger and more diverse collection.



### Limited Retrieval Methods



Only BM25 and TF-IDF were tested. Dense embedding retrieval and hybrid retrieval were not included.



## 13. Final Conclusion



The experiment shows that retrieval design should be selected according to the goal of the RAG system.



BM25 performed best for Top-1 ranking with 83.33% accuracy.



TF-IDF performed best for Top-3 evidence coverage with 100.00% accuracy.



The ablation experiment showed that increasing the retrieval window from k=1 to k=3 improved evidence coverage, while increasing it further to k=5 did not improve the results.



Therefore, for this chosen document collection, TF-IDF with k=3 gives the most reliable grounded retrieval because it consistently places the correct evidence within the retrieved context.



The evidence supporting this conclusion is the 100.00% Top-3 accuracy achieved by TF-IDF compared with 91.67% for BM25.



