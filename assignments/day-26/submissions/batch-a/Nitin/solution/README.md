\# Day 26 - End-to-End AI Capstone



\## Project Title



AI Study Assistant



\## 1. Project Overview



The AI Study Assistant is a lightweight educational AI prototype designed

to help students get quick answers to common Computer Science and Artificial

Intelligence questions.



The prototype accepts a student's question, checks it for sensitive or

private information, searches a small educational knowledge base, estimates

confidence, and returns an answer.



The system is designed as a realistic local prototype rather than a

production-scale generative AI system.



\## 2. Problem Statement



Students often need quick explanations while studying topics such as:



\- Artificial Intelligence

\- Machine Learning

\- Python

\- Pandas

\- NumPy

\- Databases

\- APIs

\- Cybersecurity



The objective is to provide a simple assistant that:



1\. answers supported educational questions;

2\. avoids inventing information when knowledge is unavailable;

3\. blocks requests involving private credentials;

4\. records evaluation evidence;

5\. remains fast and reproducible on a local computer.



\## 3. Target Users



Primary users:



\- College students

\- Beginners learning programming

\- AI and ML learners

\- Classroom learners



Potential future users:



\- Teachers

\- Training institutes

\- Educational support systems



\## 4. Success Criteria



The prototype is considered successful when it:



\- identifies supported topics correctly;

\- provides useful answers;

\- blocks sensitive credential requests;

\- refuses unsupported questions instead of hallucinating;

\- maintains low response latency;

\- produces reproducible evaluation results.



\## 5. Prototype Architecture



The system follows this flow:



User Question

&#x20;     |

&#x20;     v

Safety / Privacy Guardrail

&#x20;     |

&#x20;     +---- Sensitive request ----> Block

&#x20;     |

&#x20;     v

Question Processing

&#x20;     |

&#x20;     v

Knowledge Retrieval

&#x20;     |

&#x20;     +---- Match found ---------> Retrieve answer

&#x20;     |

&#x20;     +---- No match ------------> Uncertainty response

&#x20;     |

&#x20;     v

Confidence Estimation

&#x20;     |

&#x20;     v

Final Answer





Main components:



\- User interface: Command-line interface

\- Application logic: prototype.py

\- Knowledge base: in-memory Python data

\- Evaluation dataset: test\_scenarios.csv

\- Evaluation evidence: evaluation\_results.csv

\- Architecture documentation: architecture.txt



\## 6. Model and Technology Choice



This prototype uses a lightweight retrieval-based approach instead of a

large language model.



Technologies:



\- Python

\- CSV

\- Standard Python libraries

\- Local knowledge base

\- Rule-based privacy guardrails



This design was selected because it is:



\- inexpensive;

\- fast;

\- easy to understand;

\- easy to reproduce;

\- suitable for classroom demonstration.



A future production version could use embeddings, vector search, and a

validated language model.



\## 7. Dataset



The evaluation dataset is a manually designed benchmark containing

22 scenarios.



The scenarios include:



\- easy educational questions;

\- medium-level conceptual questions;

\- hard application-oriented questions;

\- privacy and security tests;

\- unknown-knowledge tests.



The dataset is stored in:



test\_scenarios.csv



\## 8. Evaluation



The prototype was evaluated on 22 scenarios.



The evaluation includes:



\- topic prediction correctness;

\- response success;

\- confidence score;

\- response latency;

\- reason for the response.



Results are stored in:



evaluation\_results.csv



\### Observed Evaluation



Total scenarios: 22



Correct topic predictions: 18



Topic accuracy:



18 / 22 = 81.82%



The system correctly handled all three sensitive-information

guardrail scenarios.



It also correctly refused the unknown knowledge-base request.



Several medium-level questions produced a broader "machine learning"

topic instead of the more specific expected topic such as

"supervised learning" or "unsupervised learning". These cases demonstrate

a limitation of simple keyword retrieval.



\## 9. Quantitative Metrics



\### Metric 1 - Topic Accuracy



Topic accuracy measures whether the predicted topic matches the expected

topic in the evaluation dataset.



Observed result:



81.82%



\### Metric 2 - Safety Handling



The prototype correctly blocked:



\- private key request;

\- API key request;

\- password request.



This demonstrates that the privacy guardrail is functioning for the

tested patterns.



\### Metric 3 - Latency



The local prototype produced responses in the microsecond range during

the evaluation because it uses in-memory retrieval and does not call a

remote model or API.



Latency should not be directly compared with production LLM latency because

the prototype performs much less computation.



\## 10. Qualitative Review Criteria



The system should be reviewed using these criteria:



1\. Answer relevance

2\. Answer correctness

3\. Clarity for students

4\. Appropriate uncertainty handling

5\. Privacy and security behavior



Additional production criteria should include accessibility, educational

quality, harmful-content handling, and consistency.



\## 11. Security and Privacy



The prototype includes a privacy guardrail that blocks requests containing

terms associated with sensitive credentials.



Examples include:



\- passwords;

\- private keys;

\- API keys;

\- OTPs;

\- credit-card information.



Production deployment should additionally use:



\- environment variables for secrets;

\- encrypted storage;

\- access control;

\- authentication;

\- data minimization;

\- log redaction;

\- secure API communication;

\- limited retention of student data.



Private credentials must never be stored in source code, CSV files,

evaluation logs, or Git repositories.



\## 12. Known Limitations



The current prototype has several limitations:



1\. Retrieval is keyword based.

2\. It does not understand deep semantic similarity.

3\. The knowledge base is small.

4\. Answers are manually written.

5\. Confidence is heuristic rather than statistically calibrated.

6\. The prototype does not use a large language model.

7\. There is no persistent database.

8\. There is no authentication system.

9\. There is no production monitoring service.

10\. Multilingual questions are not specifically optimized.



\## 13. How to Run



Open PowerShell in the solution directory.



Run:



python prototype.py



The program first evaluates the 22 test scenarios.



After evaluation, it starts interactive mode.



Example:



Student: What is machine learning?



The assistant returns:



\- answer;

\- topic;

\- confidence;

\- latency.



Type:



exit



to close the interactive session.



\## 14. Reproduce Evaluation



Ensure these files are present:



prototype.py

test\_scenarios.csv



Run:



python prototype.py



The evaluation output will be written to:



evaluation\_results.csv



\## 15. Production Improvement Plan



Before production deployment, the following improvements are recommended:



1\. Replace keyword matching with embedding-based retrieval.

2\. Add a larger verified educational knowledge base.

3\. Add source citations to generated answers.

4\. Add confidence calibration.

5\. Add human review for low-confidence answers.

6\. Add authentication and authorization.

7\. Add encrypted storage.

8\. Add monitoring and quality dashboards.

9\. Add model and dataset versioning.

10\. Add rollback capability.

11\. Add multilingual support.

12\. Add automated regression testing.



\## 16. Go / No-Go Decision



Decision: GO FOR LIMITED PILOT



The prototype is suitable for a controlled classroom pilot because:



\- it has been evaluated on 22 scenarios;

\- it achieved 81.82% topic accuracy;

\- sensitive credential requests were blocked;

\- unsupported questions were not answered with fabricated content;

\- local latency is very low;

\- the system is inexpensive and reproducible.



However, it is NOT ready for unrestricted production deployment.



The main reason is the limitation of keyword-based retrieval and the small

knowledge base. A production system should improve semantic retrieval,

source grounding, monitoring, privacy controls, and human oversight before

being deployed widely.



\## 17. Conclusion



The project demonstrates an end-to-end AI prototype including input

handling, safety controls, retrieval, confidence estimation, evaluation,

evidence collection, and deployment planning.



The evaluation shows that a lightweight architecture can be useful for a

limited educational pilot, but additional engineering and validation are

required before production use.

