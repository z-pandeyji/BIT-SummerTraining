\# Day 24 — Prompting, Fine-Tuning, and Adaptation Strategy



\## Topic



\*\*Prompting vs Model Adaptation for Sentiment Classification\*\*



\## 1. Project Overview



This project investigates whether prompt engineering is sufficient for a small sentiment classification task or whether model adaptation is justified.



Three approaches were considered:



1\. \*\*Zero-shot prompting\*\* — classification using a pretrained natural-language-inference model without task-specific training.

2\. \*\*Few-shot prompting\*\* — classification using examples included in the prompt.

3\. \*\*Parameter-efficient fine-tuning\*\* — a proposed LoRA-based adaptation strategy.



The experiment uses a small evaluation dataset containing \*\*51 labelled examples\*\*.



The main research question is:



> For the chosen task, is prompting sufficient, or is model adaptation justified? Defend your answer with evidence, cost, and risk analysis.



\---



\## 2. Task



\### Task: Sentiment Classification



The system classifies short text examples into sentiment categories.



The evaluation dataset contains labelled examples designed to represent positive and negative sentiment.



\### Success Metric



The primary metric is \*\*accuracy\*\*:



```text

Accuracy = Correct Predictions / Total Predictions

```



Accuracy is appropriate for this small balanced evaluation experiment because the goal is to compare the classification approaches on the same labelled examples.



\### Failure Cost



A wrong sentiment classification can lead to:



\* incorrect customer feedback analysis;

\* poor prioritization of negative reviews;

\* incorrect business decisions;

\* inaccurate reporting of user satisfaction.



For a production system, additional metrics such as precision, recall, F1-score and class-specific error rates should also be monitored.



\---



\## 3. Dataset



File:



```text

evaluation\_dataset.csv

```



Number of labelled examples:



```text

51

```



The dataset is a small evaluation set created for this experiment. It is intended for classroom experimentation rather than production benchmarking.



Each example contains text and its expected sentiment label.



\---



\## 4. Experimental Approaches



\### Approach 1 — Zero-shot prompting



A pretrained classification model is used directly without task-specific fine-tuning.



The model receives the input text and candidate sentiment labels and predicts the most appropriate label.



Advantages:



\* no training required;

\* fast to deploy;

\* easy to reproduce;

\* low development cost.



\---



\### Approach 2 — Few-shot prompting



The model is provided with labelled examples before making predictions.



The purpose is to determine whether giving demonstrations improves task performance compared with zero-shot classification.



Advantages:



\* no parameter training;

\* easy to modify;

\* can adapt prompts to a specific task.



Disadvantages:



\* prompt design can strongly affect results;

\* additional examples increase prompt size;

\* performance may vary depending on the selected demonstrations.



\---



\### Approach 3 — Parameter-efficient fine-tuning



The third approach was designed as an adaptation plan using \*\*LoRA (Low-Rank Adaptation)\*\*.



Instead of updating the entire pretrained model, LoRA trains a relatively small number of additional parameters.



This approach was planned rather than executed locally because full model adaptation can require considerably more compute and setup than the baseline experiments.



\---



\## 5. Results



The experiments produced the following results:



| Approach                        | Accuracy | Average Latency | Cost       | Privacy                 | Maintainability | Reproducibility |

| ------------------------------- | -------: | --------------: | ---------- | ----------------------- | --------------- | --------------- |

| Zero-shot prompting             |   1.0000 |        0.9049 s | Low        | Medium                  | High            | High            |

| Few-shot prompting              |   0.4314 |        1.7124 s | Low-Medium | Medium                  | Medium-High     | High            |

| Parameter-efficient fine-tuning |  Planned |         Planned | Medium     | High if locally trained | Medium          | Medium-High     |



\### Interpretation



Zero-shot prompting achieved the highest measured accuracy in this experiment:



```text

100%

```



Few-shot prompting achieved:



```text

43.14%

```



Therefore, adding examples to the prompt did \*\*not\*\* improve performance on this particular evaluation dataset.



This result should not be interpreted as proof that zero-shot prompting is always superior to few-shot prompting. The evaluation set is small, and prompt construction and model behaviour can significantly influence the result.



\---



\## 6. Reproducibility



Activate the virtual environment and navigate to the solution directory.



Install the required packages if necessary:



```bash

python -m pip install pandas numpy scikit-learn torch transformers datasets

```



Run the experiment:



```bash

python adaptation\_experiment.py

```



The script reads:



```text

evaluation\_dataset.csv

```



and produces:



```text

comparison\_results.csv

```



The results table contains the measured performance and qualitative comparison of the three approaches.



\---



\## 7. Files



```text

solution/

│

├── adaptation\_experiment.py

├── evaluation\_dataset.csv

├── comparison\_results.csv

├── README.md

└── report.md

```



\### File descriptions



\*\*adaptation\_experiment.py\*\*



Contains the experimental implementation and evaluation logic.



\*\*evaluation\_dataset.csv\*\*



Contains the 51 labelled evaluation examples.



\*\*comparison\_results.csv\*\*



Contains the comparison between zero-shot, few-shot and planned parameter-efficient fine-tuning.



\*\*README.md\*\*



Contains setup and reproduction instructions.



\*\*report.md\*\*



Contains the detailed technical research report and analysis.



\---



\## 8. Limitations



This experiment has several limitations:



1\. The evaluation dataset contains only 51 examples.

2\. The dataset is intended for educational experimentation.

3\. Only accuracy is used as the primary quantitative metric.

4\. Fine-tuning was designed but not executed.

5\. Model behaviour can change with different prompts, models and datasets.

6\. Latency measurements depend on the local hardware and environment.

7\. The results should not be treated as production-level benchmarking.



\---



\## 9. Conclusion



For this experiment, \*\*zero-shot prompting was sufficient\*\* and produced the strongest measured result.



Because zero-shot prompting achieved 100% accuracy on the evaluation dataset while requiring low cost and high maintainability, immediate fine-tuning is not justified for this small classroom scenario.



However, model adaptation could become justified if a larger representative dataset reveals systematic errors that prompting cannot solve.



The recommended strategy is therefore:



```text

Start with zero-shot prompting

&#x20;       ↓

Evaluate on a representative dataset

&#x20;       ↓

Analyze failures

&#x20;       ↓

Improve prompting/retrieval if necessary

&#x20;       ↓

Consider LoRA fine-tuning only when evidence supports it

```



