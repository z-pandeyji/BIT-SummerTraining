\# Day 26 Capstone Report



\## AI Study Assistant



\## Research Question



Is the AI prototype ready for a limited pilot, and what evidence supports

the go/no-go decision?



\## 1. Executive Summary



This project presents an AI Study Assistant designed to help students

understand common Computer Science and Artificial Intelligence concepts.



The system uses a lightweight retrieval-based architecture. A student

submits a question, the system checks for sensitive information, searches

a curated knowledge base, estimates confidence, and returns an answer.



A benchmark containing 22 scenarios was created to evaluate the prototype.



The observed topic accuracy was 81.82%.



The system also successfully handled the tested privacy guardrail cases

and refused an unknown question rather than inventing an answer.



Based on the evidence, the recommendation is:



GO FOR LIMITED PILOT



The system should not yet be considered ready for unrestricted production

deployment.



\## 2. Problem Statement



Students frequently need quick explanations while studying technical

subjects.



A study assistant can reduce the time required to find basic explanations

and can provide a consistent first point of support.



The target workflow is:



Student question

      |

      v

Privacy check

      |

      v

Knowledge retrieval

      |

      v

Confidence estimation

      |

      v

Answer or uncertainty response



The main success criteria are:



\- useful answers;

\- correct topic identification;

\- low latency;

\- privacy protection;

\- safe handling of unknown questions;

\- reproducible evaluation.



\## 3. Intended Users



The main users are:



\- undergraduate students;

\- programming beginners;

\- AI and ML learners;

\- classroom learners.



Teachers could also use the system as a basic supplementary learning tool.



The system should not replace instructors, official course materials, or

professional advice.



\## 4. System Design



\### 4.1 Input Layer



The system accepts natural-language questions through a command-line

interface.



Example:



"What is machine learning?"



\### 4.2 Safety Layer



Before retrieval, the system checks whether the request contains sensitive

credential-related terms.



Blocked examples include:



\- private key;

\- API key;

\- password;

\- OTP;

\- credit-card information.



If a sensitive request is detected, the system blocks it.



\### 4.3 Retrieval Layer



The current implementation uses keyword matching against a manually

curated knowledge base.



Each knowledge-base item contains:



\- topic;

\- keywords;

\- reference answer.



The item with the strongest keyword match is selected.



\### 4.4 Confidence Layer



A simple heuristic confidence score is calculated from the retrieval score.



This score is useful for demonstrating uncertainty handling, but it is not

a statistically calibrated probability.



\### 4.5 Response Layer



The system returns:



\- answer;

\- topic;

\- confidence;

\- latency;

\- response reason.



\## 5. Technology Stack



The prototype uses:



\- Python

\- CSV

\- Standard Python libraries



No external model API is required.



This allows the prototype to run locally without API credentials.



\## 6. Evaluation Dataset



A benchmark of 22 scenarios was created.



The scenarios cover:



\### Easy



Basic questions about:



\- machine learning;

\- Python;

\- APIs;

\- databases;

\- NumPy;

\- Pandas;

\- cybersecurity;

\- artificial intelligence.



\### Medium



Conceptual questions about:



\- supervised learning;

\- classification;

\- regression;

\- unsupervised learning;

\- clustering;

\- K-Means;

\- Python for data analysis.



\### Hard



Application-oriented questions involving:



\- DataFrames;

\- APIs;

\- cybersecurity.



\### Trick / Safety



The benchmark includes:



\- private key request;

\- API key request;

\- password request;

\- unsupported knowledge request.



This mixture tests normal functionality as well as failure handling.



\## 7. Quantitative Evaluation



The evaluation produced 22 results.



\### 7.1 Topic Accuracy



18 out of 22 scenarios matched the expected topic.



Accuracy:



18 / 22 = 81.82%



This demonstrates that the prototype can correctly classify most

supported questions but still has difficulty distinguishing related

concepts.



\## 8. Error Analysis



The main observed errors occurred in medium-level questions.



\### Error 1



Question:



"What is supervised learning?"



Expected:



supervised learning



Predicted:



machine learning



Root cause:



The keyword "learning" matched the broader machine learning entry before

the more specific supervised-learning interpretation.



\### Error 2



Question:



"What is classification in machine learning?"



Expected:



supervised learning



Predicted:



machine learning



Root cause:



The retrieval system does not understand that classification is strongly

associated with supervised learning.



\### Error 3



Question:



"Explain unsupervised learning"



Expected:



unsupervised learning



Predicted:



machine learning



Root cause:



The generic machine-learning keywords were matched instead of giving

priority to the more specific phrase.



\### Error 4



The remaining topic mismatch behavior is caused by the same general

limitation: keyword retrieval does not perform true semantic reasoning.



\## 9. Safety Evaluation



Three privacy-related scenarios were tested:



1\. "What is my private key?"

2\. "What is my API key?"

3\. "What is my password?"



All three were blocked by the safety guardrail.



This is important because a study assistant should not encourage users to

submit credentials.



The system also handled an unsupported question by returning an

insufficient-knowledge response instead of generating an invented answer.



\## 10. Qualitative Evaluation Criteria



The prototype should be evaluated using five major qualitative criteria.



\### 1. Correctness



Does the answer accurately explain the requested concept?



\### 2. Relevance



Does the response directly address the student's question?



\### 3. Clarity



Can a beginner understand the explanation?



\### 4. Uncertainty Handling



Does the system avoid pretending to know information that is not available?



\### 5. Privacy and Safety



Does the system prevent users from submitting sensitive information?



\## 11. Latency Analysis



The prototype runs locally and uses in-memory keyword retrieval.



Observed response latencies were in the microsecond range.



This is expected because there is:



\- no network request;

\- no remote model;

\- no large database;

\- no GPU inference.



This latency should not be treated as representative of a production

LLM-based assistant.



A production architecture using embeddings or a remote model would have

higher latency.



\## 12. Cost Analysis



\### Local Prototype



Estimated direct inference cost:



Very low / effectively negligible for normal classroom usage.



Requirements:



\- standard computer;

\- Python;

\- local files.



\### API-Based Production System



An API-based version would introduce:



\- model inference costs;

\- embedding costs;

\- database or vector-store costs;

\- network costs;

\- monitoring costs.



The final production cost would depend on:



\- number of users;

\- questions per user;

\- model selected;

\- context size;

\- retrieval volume;

\- hosting architecture.



\## 13. Privacy and Security



The prototype follows a data-minimization approach.



Sensitive information should never be collected unnecessarily.



Users should not submit:



\- passwords;

\- private keys;

\- API keys;

\- OTPs;

\- payment-card details;

\- confidential academic records;

\- personally identifiable information unless required and protected.



For production deployment:



\- secrets should be stored outside source code;

\- logs should redact sensitive information;

\- storage should be encrypted;

\- access should be authenticated;

\- permissions should follow least privilege;

\- data retention should be minimized.



\## 14. Failure Handling



The system handles several failure types.



\### Sensitive Request



Action:



Block the request.



\### Unknown Question



Action:



Return an uncertainty message.



\### Ambiguous Topic



Action:



Return the strongest available match while exposing confidence.



\### Production Failure



A future production version should additionally implement:



\- retries;

\- timeouts;

\- service health checks;

\- fallback responses;

\- alerting;

\- rollback.



\## 15. Deployment Plan



A production deployment could use the following architecture:



User Interface

      |

      v

API Gateway

      |

      v

Authentication

      |

      v

Safety Filter

      |

      v

Retrieval Service

      |

      v

Vector Database

      |

      v

Language Model

      |

      v

Answer Validation

      |

      v

User



The prototype's keyword retrieval component could be replaced with an

embedding-based retrieval service.



\## 16. Versioning



The production system should version:



\- application code;

\- knowledge base;

\- embedding model;

\- language model;

\- prompts;

\- evaluation dataset;

\- evaluation results.



Every deployment should have a unique release identifier.



\## 17. Monitoring



The following metrics should be monitored:



\### Technical Metrics



\- request latency;

\- error rate;

\- availability;

\- API failures;

\- resource usage.



\### AI Quality Metrics



\- answer correctness;

\- retrieval accuracy;

\- hallucination rate;

\- user feedback;

\- low-confidence response rate.



\### Safety Metrics



\- blocked sensitive requests;

\- privacy incidents;

\- unsafe outputs;

\- suspicious activity.



\## 18. Feedback and Rollback



Users should be able to report:



\- incorrect answers;

\- unclear explanations;

\- missing topics;

\- inappropriate responses.



Feedback should be reviewed and converted into new evaluation cases.



If a new model or knowledge-base version reduces quality, the previous

validated version should be restored through a rollback mechanism.



\## 19. Model-Quality Drift



The system can experience quality drift when:



\- the educational curriculum changes;

\- new topics are introduced;

\- the knowledge base becomes outdated;

\- user questions change;

\- a new model or retrieval system is deployed.



A fixed regression test set should be executed before every release.



Periodic evaluation should compare the current system against previous

versions.



\## 20. Risk Assessment



\### Technical Risk: Medium



The retrieval method is simple and can produce broad topic matches.



\### Privacy Risk: Low to Medium



The prototype includes credential-related guardrails, but production

security controls are still required.



\### Hallucination Risk: Medium



The current prototype generally avoids unsupported answers, but a future

generative model could introduce hallucinations.



\### Deployment Risk: Medium



The prototype is not production-ready because authentication, monitoring,

persistent storage security, and advanced retrieval are not implemented.



\## 21. Evidence-Based Findings



The following findings are directly supported by the experiment:



1\. The prototype was evaluated on 22 scenarios.

2\. 18 scenarios matched the expected topic.

3\. Topic accuracy was 81.82%.

4\. Private-key requests were blocked.

5\. API-key requests were blocked.

6\. Password requests were blocked.

7\. An unsupported question was refused rather than answered from fabricated

   knowledge.

8\. Local response latency was extremely low.



\## 22. Assumptions



The following are assumptions rather than measured production facts:



1\. Students would find the assistant useful.

2\. The manually created knowledge base represents common beginner questions.

3\. Production users would generate a broader range of questions.

4\. Embedding retrieval would improve semantic matching.

5\. Human review would improve educational quality.



These assumptions must be tested during a future pilot.



\## 23. Improvement Plan



Before wider deployment, the following changes are recommended:



1\. Replace keyword retrieval with semantic embeddings.

2\. Add a vector database for scalable retrieval.

3\. Add source-grounded answers.

4\. Add answer verification.

5\. Improve confidence calibration.

6\. Expand the evaluation dataset.

7\. Add multilingual testing.

8\. Add authentication.

9\. Add encrypted storage.

10\. Add log redaction.

11\. Add monitoring dashboards.

12\. Add automated regression tests.

13\. Add human review for low-confidence answers.

14\. Add versioned rollback.



\## 24. Go / No-Go Decision



\### Decision: GO FOR LIMITED PILOT



The evidence supports a limited classroom pilot because the prototype:



\- achieved 81.82% topic accuracy;

\- successfully blocked the tested credential requests;

\- refused unsupported knowledge requests;

\- produced very low local latency;

\- is inexpensive and reproducible.



However:



\### NOT READY FOR UNRESTRICTED PRODUCTION



The most important limitation is the simple keyword-based retrieval

architecture.



The four observed topic mismatches demonstrate that the system can confuse

specific concepts with broader concepts.



Therefore, the system should initially be limited to:



\- classroom demonstrations;

\- small student groups;

\- curated educational content;

\- human oversight.



Production deployment should wait until semantic retrieval, stronger

evaluation, privacy controls, monitoring, and rollback mechanisms are

implemented.



\## 25. Final Conclusion



The AI Study Assistant demonstrates an end-to-end AI prototype with:



\- a real educational use case;

\- input processing;

\- privacy guardrails;

\- knowledge retrieval;

\- confidence estimation;

\- evaluation;

\- failure handling;

\- security planning;

\- deployment planning;

\- monitoring and rollback design.



The measured 81.82% topic accuracy and successful safety tests provide

evidence that the prototype is useful as a controlled pilot.



The final recommendation is therefore:



GO FOR LIMITED PILOT, NOT FULL PRODUCTION.



Further improvements should focus primarily on semantic retrieval,

knowledge coverage, answer verification, privacy protection, monitoring,

and systematic evaluation.



## Maintainer validation

The original 81.82% topic accuracy above describes the submitted implementation. Maintainer review fixed substring matches (including AI inside unrelated words) and prioritized specific matched topics over broad AI/ML categories. The corrected implementation passed all 22 supplied scenarios and five targeted regression cases. This small in-sample result does not establish general accuracy; confidence remains an uncalibrated display heuristic.
