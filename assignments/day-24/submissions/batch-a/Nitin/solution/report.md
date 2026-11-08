\# Day 24 Research Report



\## Prompting, Fine-Tuning, and Adaptation Strategy



\### Research Question



> \*\*For your chosen task, is prompting sufficient, or is model adaptation justified? Defend your answer with evidence, cost, and risk analysis.\*\*



\---



\# 1. Executive Summary



This study compares prompting-based approaches with model adaptation for a small sentiment classification task.



Three strategies were investigated:



1\. zero-shot prompting;

2\. few-shot prompting;

3\. parameter-efficient fine-tuning using a proposed LoRA strategy.



A labelled evaluation dataset containing 51 examples was used for the baseline experiments.



The measured results show that zero-shot classification achieved \*\*100% accuracy\*\*, while the few-shot approach achieved \*\*43.14% accuracy\*\*.



The zero-shot approach also had lower measured latency and lower operational complexity.



Based on this experiment, prompting is sufficient for the selected classroom-scale task, and immediate model adaptation is not justified.



However, this conclusion is limited by the small evaluation dataset. A larger representative benchmark would be required before making a production deployment decision.



\---



\# 2. Task Description



\## 2.1 Selected Task



The selected task is:



\*\*Sentiment Classification\*\*



The objective is to determine the sentiment expressed by a short text example.



The experiment focuses on comparing different methods for solving the same classification problem.



\---



\## 2.2 Why This Task Was Selected



Sentiment classification is a useful example for studying prompting and model adaptation because:



\* pretrained language models can perform the task without training;

\* examples can be provided through few-shot prompting;

\* labelled datasets can be used for supervised adaptation;

\* classification errors can affect downstream business decisions.



Potential applications include:



\* customer feedback analysis;

\* product review analysis;

\* social media monitoring;

\* support-ticket prioritization;

\* satisfaction analysis.



\---



\# 3. Evaluation Dataset



The experiment uses:



```text

evaluation\_dataset.csv

```



The dataset contains:



```text

51 labelled examples

```



The dataset was designed as a small educational evaluation benchmark.



Each example contains an input text and its expected sentiment label.



The same evaluation examples were used to compare the approaches so that the results could be compared consistently.



\---



\# 4. Success Metric



The primary metric is classification accuracy.



The formula is:



```text

Accuracy = Correct Predictions / Total Predictions

```



Accuracy was selected because the experiment focuses on direct comparison of predictions against known labels.



For a production sentiment system, accuracy alone would not be sufficient. Precision, recall, F1-score and confusion matrices should also be examined.



\---



\# 5. Failure Cost



A sentiment classifier can produce incorrect business conclusions when it misclassifies text.



Examples include:



\* treating a negative customer complaint as positive;

\* failing to identify dissatisfied users;

\* incorrectly prioritizing customer feedback;

\* generating misleading business reports.



Therefore, model errors should be reviewed before deployment in a real business environment.



\---



\# 6. Approach 1 — Zero-Shot Prompting



\## 6.1 Method



The first approach uses a pretrained language model directly.



No task-specific training data is used during model adaptation.



The model is asked to classify the input according to the available sentiment labels.



This represents the simplest deployment strategy.



\---



\## 6.2 Advantages



Zero-shot prompting provides:



\* low development cost;

\* no training pipeline;

\* simple deployment;

\* high maintainability;

\* good reproducibility.



It is especially useful when the task is simple and a suitable pretrained model already exists.



\---



\# 7. Approach 2 — Few-Shot Prompting



\## 7.1 Method



The second approach provides labelled examples to the model before evaluating new examples.



The intention is to demonstrate the desired classification behaviour through examples.



Few-shot prompting can be useful when the task requires additional context or when label definitions are difficult to express through a short instruction.



\---



\## 7.2 Experimental Result



The measured accuracy was:



```text

43.14%

```



The average latency was:



```text

1.7124 seconds

```



The measured result was lower than the zero-shot baseline.



This indicates that the selected few-shot prompt did not improve performance on this evaluation set.



\---



\# 8. Approach 3 — Parameter-Efficient Fine-Tuning



\## 8.1 Proposed Method



The third approach is parameter-efficient fine-tuning using \*\*LoRA (Low-Rank Adaptation)\*\*.



Instead of updating all model parameters, LoRA adds trainable low-rank components to selected model layers.



The intended workflow is:



```text

Pretrained model

&#x20;      ↓

Prepare labelled sentiment dataset

&#x20;      ↓

Tokenization

&#x20;      ↓

Attach LoRA adapters

&#x20;      ↓

Train adapters

&#x20;      ↓

Evaluate on held-out test data

&#x20;      ↓

Compare with prompting baseline

```



\---



\## 8.2 Why LoRA Was Selected



Full model fine-tuning can require substantial memory and compute resources.



LoRA can reduce the number of trainable parameters and therefore make adaptation more practical on limited hardware.



For this assignment, the LoRA approach was designed but not executed as a full training experiment.



\---



\# 9. Quantitative Comparison



The experimental results were:



| Approach            | Accuracy | Average Latency | Cost       |

| ------------------- | -------: | --------------: | ---------- |

| Zero-shot prompting |  100.00% |        0.9049 s | Low        |

| Few-shot prompting  |   43.14% |        1.7124 s | Low-Medium |

| LoRA fine-tuning    |  Planned |         Planned | Medium     |



The broader engineering comparison was:



| Factor          | Zero-shot     | Few-shot        | LoRA                    |

| --------------- | ------------- | --------------- | ----------------------- |

| Accuracy        | 100% measured | 43.14% measured | Not measured            |

| Cost            | Low           | Low-Medium      | Medium                  |

| Latency         | 0.9049 s      | 1.7124 s        | Planned                 |

| Maintainability | High          | Medium-High     | Medium                  |

| Privacy         | Medium        | Medium          | High if trained locally |

| Reproducibility | High          | High            | Medium-High             |



\---



\# 10. Result Analysis



\## 10.1 Zero-Shot Performance



Zero-shot classification achieved:



```text

Accuracy = 1.0000

```



This was the strongest measured result.



The result suggests that the pretrained model already had sufficient general knowledge for the selected evaluation examples.



\---



\## 10.2 Few-Shot Performance



Few-shot classification achieved:



```text

Accuracy = 0.4314

```



This was substantially lower than the zero-shot result.



This demonstrates an important point:



> Adding examples to a prompt does not automatically improve model performance.



The quality, selection and formatting of demonstrations can strongly affect few-shot results.



\---



\## 10.3 Latency



Measured average latency:



```text

Zero-shot:  0.9049 seconds

Few-shot:   1.7124 seconds

```



The few-shot approach was slower in this experiment.



A larger prompt requires more input processing and can increase inference latency.



\---



\# 11. Qualitative Error Analysis



At least ten difficult or failed cases should be reviewed when this system is extended to a larger evaluation dataset.



Important categories for manual review include:



\### 1. Negation



Example:



```text

"The product is not good."

```



A model may incorrectly focus on the word "good" instead of the negation.



\### 2. Mixed sentiment



Example:



```text

"The design is excellent, but the battery is disappointing."

```



The text contains both positive and negative signals.



\### 3. Sarcasm



Example:



```text

"Great, another update that broke everything."

```



The literal word "Great" may suggest positive sentiment even though the intended meaning is negative.



\### 4. Ambiguous wording



Some sentences do not clearly express a positive or negative opinion.



\### 5. Domain-specific language



Words may have different meanings in different domains.



\### 6. Short inputs



Very short text can lack enough context for reliable classification.



\### 7. Multiple opinions



A single sentence can contain opinions about multiple aspects of a product.



\### 8. Informal language



Internet slang, abbreviations and emojis can make classification more difficult.



\### 9. Spelling errors



Misspelled words can reduce model confidence.



\### 10. Context-dependent sentiment



The sentiment of a sentence can depend on information that is not explicitly included in the sentence.



These categories should be included in future testing even if the small evaluation set produces few obvious errors.



\---



\# 12. Cost Analysis



\## Zero-Shot



Estimated relative cost:



\*\*Low\*\*



Reasons:



\* no training;

\* minimal data preparation;

\* simple inference pipeline;

\* easy deployment.



\---



\## Few-Shot



Estimated relative cost:



\*\*Low-Medium\*\*



Reasons:



\* no model training;

\* larger prompts;

\* increased input processing;

\* prompt engineering effort.



\---



\## LoRA Fine-Tuning



Estimated relative cost:



\*\*Medium\*\*



Additional requirements include:



\* labelled training data;

\* validation and test splits;

\* GPU or suitable compute;

\* training time;

\* experiment tracking;

\* model versioning;

\* evaluation after training.



\---



\# 13. Privacy Analysis



Privacy must be considered before using real customer or user data.



The following information should generally \*\*not\*\* be submitted unnecessarily to an AI system:



\* passwords;

\* authentication tokens;

\* API keys;

\* bank account information;

\* credit/debit card details;

\* government identification numbers;

\* private addresses;

\* confidential company documents;

\* private customer conversations;

\* sensitive personal information.



Data should be minimized and anonymized whenever possible.



If model adaptation is performed on sensitive organizational data, local or controlled training environments may provide stronger privacy guarantees than sending the raw data to an external service.



\---



\# 14. Maintainability



\## Zero-Shot



High maintainability.



The system can be changed by modifying the task instructions or model configuration.



No training pipeline is required.



\## Few-Shot



Medium-High maintainability.



Examples can be changed easily, but prompt quality must be monitored.



\## LoRA



Medium maintainability.



A training pipeline, adapter versioning and model evaluation process are required.



\---



\# 15. Reproducibility



The baseline experiments are highly reproducible because:



\* the evaluation dataset is included;

\* the experiment code is included;

\* the comparison results are saved;

\* the same evaluation data can be reused.



Fine-tuning would require additional documentation of:



\* model version;

\* dataset version;

\* training parameters;

\* random seeds;

\* hardware;

\* number of epochs;

\* learning rate;

\* LoRA configuration.



\---



\# 16. Evidence-Based Findings vs Assumptions



\## Evidence-Based Findings



The following conclusions are directly supported by the experiment:



1\. The evaluation dataset contains 51 examples.

2\. Zero-shot accuracy was 100%.

3\. Few-shot accuracy was 43.14%.

4\. Zero-shot average latency was 0.9049 seconds.

5\. Few-shot average latency was 1.7124 seconds.

6\. Zero-shot had the strongest measured performance among the executed approaches.



\## Assumptions / Limitations



The following should not be treated as experimentally proven:



1\. Zero-shot prompting will always outperform few-shot prompting.

2\. The same accuracy will occur on a larger dataset.

3\. LoRA will necessarily outperform prompting.

4\. The measured latency will remain identical on other hardware.

5\. The model will behave identically on a different domain.



These require additional testing.



\---



\# 17. When Is Model Adaptation Justified?



Model adaptation becomes more reasonable when:



\* prompting produces repeated systematic errors;

\* a large high-quality labelled dataset is available;

\* the task is domain-specific;

\* consistent terminology is required;

\* privacy requirements favour controlled local training;

\* inference efficiency needs to be optimized;

\* prompt engineering has reached its practical limit.



Fine-tuning should not be performed simply because it is technically possible.



It should be supported by evidence that prompting is insufficient.



\---



\# 18. Recommendation for a Real Scenario



Consider a college or small business that needs to classify customer feedback.



The recommended approach is:



\### Phase 1



Start with zero-shot prompting.



\### Phase 2



Evaluate on a representative labelled dataset.



\### Phase 3



Perform error analysis.



\### Phase 4



Improve the prompt or add retrieval/context if necessary.



\### Phase 5



Only consider LoRA fine-tuning if systematic errors remain and enough high-quality labelled data is available.



For the current classroom experiment, \*\*fine-tuning is not justified\*\* because the zero-shot baseline already achieved 100% accuracy on the available evaluation set.



\---



\# 19. Final Answer to the Research Question



\## Is prompting sufficient?



\*\*Yes, for this experimental setting.\*\*



Zero-shot prompting achieved \*\*100% accuracy\*\* on the 51-example evaluation dataset, while few-shot prompting achieved \*\*43.14%\*\*.



The zero-shot approach also had lower measured latency and lower implementation complexity.



Therefore, there is no evidence from this experiment that model adaptation is currently necessary.



However, the conclusion is limited by the small evaluation dataset.



For production deployment, a much larger and representative dataset should be evaluated. If systematic errors appear that cannot be solved through prompting or retrieval, parameter-efficient fine-tuning such as LoRA could then be justified.



The evidence-based strategy is therefore:



```text

Prompt first

&#x20;   ↓

Evaluate

&#x20;   ↓

Analyze errors

&#x20;   ↓

Improve prompting/retrieval

&#x20;   ↓

Fine-tune only if evidence justifies it

```



\---



\# 20. Sources



The following sources informed the technical approach:



1\. Hugging Face Transformers documentation

&#x20;  https://huggingface.co/docs/transformers/



2\. Hugging Face PEFT documentation

&#x20;  https://huggingface.co/docs/peft/



3\. Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models"

&#x20;  https://arxiv.org/abs/2106.09685



4\. Brown et al., "Language Models are Few-Shot Learners"

&#x20;  https://arxiv.org/abs/2005.14165



5\. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"

&#x20;  https://arxiv.org/abs/2005.11401



\---



\# 21. Conclusion



This experiment demonstrates that model adaptation should be treated as an engineering decision rather than an automatic improvement.



For the selected task and evaluation dataset, zero-shot prompting provided the best measured result with low cost and high maintainability.



Fine-tuning remains a useful future option when larger evidence demonstrates that prompting is insufficient.



The central lesson is:



> \*\*Use the simplest approach that reliably meets the required quality, privacy, cost and maintainability constraints.\*\*



