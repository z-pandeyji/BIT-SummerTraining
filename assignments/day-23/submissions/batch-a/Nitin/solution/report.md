\# Responsible AI Bias, Privacy, and Risk Audit



\## Research Question



> \*\*What are the most important responsible AI risks in the chosen system, and what evidence-based mitigations should be applied before deployment?\*\*



\## 1. System and Dataset Description



This audit examines the \*\*UCI Adult Income Dataset\*\*, a public dataset commonly used for studying income classification and machine learning fairness.



The dataset contains demographic, employment, education, and financial-related attributes. The target variable indicates whether a person's annual income is above or below $50,000.



The audit uses a simple logistic regression classifier as a baseline example of a system that could predict the income category of an individual.



Potentially affected groups include people represented by different:



\* Sex groups

\* Race groups

\* Education levels

\* Occupations

\* Employment categories

\* Marital-status groups



Because income-related prediction can influence decisions in areas such as employment, lending, insurance, or social services, demographic differences require careful examination before deployment.



\---



\## 2. Dataset and Model Card Summary



\### Dataset



\*\*Name:\*\* UCI Adult Income Dataset



\*\*Type:\*\* Tabular classification dataset



\*\*Records before cleaning:\*\* 32,561



\*\*Records after cleaning:\*\* 30,162



\*\*Target:\*\* Income category



\*\*Features:\*\* Age, education, occupation, workclass, marital status, relationship, race, sex, capital gain, capital loss, working hours, and native country.



\### Intended research use



The dataset is suitable for educational machine learning experiments, fairness analysis, and classification research.



It should not automatically be treated as representative of a modern population or used as a production decision-making dataset without additional validation.



\### Model



A logistic regression classifier was used as a simple baseline.



The model is not presented as a production-ready system. It is used only to demonstrate measurable fairness and deployment risks.



\---



\## 3. Data Quality and Missing-Value Audit



The original dataset contained missing values in several fields.



The main missing-value counts were:



| Feature        | Missing values |

| -------------- | -------------: |

| Workclass      |          1,836 |

| Occupation     |          1,843 |

| Native-country |            583 |



Other listed features did not contain missing values in this dataset.



After removing rows containing missing values, the dataset decreased from \*\*32,561 to 30,162 records\*\*.



Therefore, approximately \*\*7.37% of the original records were removed during cleaning\*\*.



\### Risk



Removing incomplete records can change the population being analyzed. If missingness is associated with demographic or socioeconomic characteristics, simply deleting those records can introduce selection bias.



\### Evidence-based finding



The missing-value pattern is directly observed from the dataset and was measured by the audit script.



\---



\## 4. Label Imbalance Audit



The income target was distributed as follows:



| Income category | Percentage |

| --------------- | ---------: |

| <=50K           |     75.11% |

| >50K            |     24.89% |



This shows a substantial class imbalance.



Approximately three quarters of the cleaned records belong to the `<=50K` class.



\### Risk



Accuracy alone can hide poor performance on the minority class. Therefore, precision and recall should also be considered when evaluating a model.



\---



\## 5. Demographic Representation Audit



\### Sex representation



| Group  | Percentage |

| ------ | ---------: |

| Male   |     67.57% |

| Female |     32.43% |



The dataset contains approximately twice as many male records as female records.



\### Race representation



| Group              | Percentage |

| ------------------ | ---------: |

| White              |     85.98% |

| Black              |      9.34% |

| Asian-Pac-Islander |      2.97% |

| Amer-Indian-Eskimo |      0.95% |

| Other              |      0.77% |



The race distribution is highly uneven, with the White category representing the large majority of records.



\### Risk



Underrepresented groups may have less reliable statistical estimates and may not be adequately represented by patterns learned from the dataset.



This creates a potential fairness and generalization risk.



\---



\## 6. Outcome Difference by Sex



The observed proportion of records with income above $50K was:



| Sex    | High-income rate |

| ------ | ---------------: |

| Female |           11.37% |

| Male   |           31.38% |



The difference between the two observed rates is:



\*\*31.38% - 11.37% = 20.01 percentage points.\*\*



The male rate is therefore substantially higher in this dataset.



\### Important interpretation



This difference is an observed association in the dataset. It does \*\*not\*\* prove that sex itself causes income differences.



Historical socioeconomic factors, occupation, education, working hours, labor-market conditions, and other variables may contribute to the observed difference.



Therefore, this result should be treated as evidence of a potential fairness concern rather than proof of intentional discrimination.



\---



\## 7. Outcome Difference by Race



Observed high-income rates were:



| Race               | High-income rate |

| ------------------ | ---------------: |

| Amer-Indian-Eskimo |           11.89% |

| Asian-Pac-Islander |           27.71% |

| Black              |           12.99% |

| Other              |            9.09% |

| White              |           26.37% |



The results show substantial differences between groups.



The highest observed rate was for the Asian-Pac-Islander category at \*\*27.71%\*\*, while the lowest was for the Other category at \*\*9.09%\*\*.



The difference is \*\*18.62 percentage points\*\*.



\### Risk



A model trained on historical data may learn or reproduce historical socioeconomic inequalities.



Demographic attributes can also act as proxies for other characteristics, meaning that removing an explicit sensitive feature does not necessarily remove all potential sources of group disparity.



\---



\## 8. Baseline Model Performance



The logistic regression model produced the following overall results:



| Metric    | Result |

| --------- | -----: |

| Accuracy  | 84.68% |

| Precision | 73.72% |

| Recall    | 59.78% |



The accuracy appears relatively high, but recall is considerably lower.



This demonstrates why multiple evaluation metrics are necessary for an imbalanced classification problem.



\### Technical limitation



The training process produced a convergence warning from the logistic regression optimizer.



This means the selected optimization configuration did not fully converge within the specified iteration limit.



The result is still useful as a baseline experiment, but a production system would require model tuning and additional validation.



\---



\## 9. Group Model Performance



The audit also compared model behavior by sex.



| Group  | Samples | Accuracy | Recall | Positive prediction rate |

| ------ | ------: | -------: | -----: | -----------------------: |

| Female |   2,446 |   91.78% | 51.88% |                    8.67% |

| Male   |   5,095 |   81.28% | 61.24% |                   25.71% |



The results show measurable differences.



Female records had higher accuracy but substantially lower recall and positive prediction rate than male records.



The positive prediction rate difference was:



\*\*25.71% - 8.67% = 17.04 percentage points.\*\*



\### Fairness interpretation



These differences indicate that aggregate model accuracy is insufficient to determine whether the system is fair.



Different groups can experience different error patterns even when the overall accuracy looks acceptable.



\---



\## 10. Privacy Risk Assessment



The dataset contains attributes that can be sensitive or potentially identifying when combined.



Examples include:



\* Age

\* Sex

\* Race

\* Native country

\* Occupation

\* Workclass

\* Education

\* Marital status

\* Financial-related attributes



Even when a dataset does not contain a person's name, combinations of attributes can increase re-identification risk in some contexts.



\### Data that should not be unnecessarily submitted to an AI system



A production AI workflow should avoid collecting or sending unnecessary:



\* Government identification numbers

\* Passwords

\* Authentication credentials

\* Bank account information

\* Credit/debit card details

\* Private medical records

\* Precise home addresses

\* Personal contact lists

\* Confidential employment records

\* Private documents containing unrelated personal information



Data minimization should be applied before sending information to an AI model or external service.



\---



\## 11. Transparency Risks



A responsible deployment should clearly communicate:



1\. What the model predicts.

2\. What data is used.

3\. Which groups may be affected.

4\. How model performance was measured.

5\. Known limitations.

6\. Whether humans review important decisions.

7\. How users can challenge or correct an incorrect result.



A model score should not automatically be treated as an objective truth.



\---



\## 12. Evidence-Based Findings vs Assumptions



\### Evidence-based findings



The following observations were directly calculated from the dataset or experiment:



\* 32,561 original records were available.

\* 30,162 records remained after removing missing rows.

\* Workclass had 1,836 missing values.

\* Occupation had 1,843 missing values.

\* Native-country had 583 missing values.

\* 75.11% of cleaned records belonged to the <=50K class.

\* 24.89% belonged to the >50K class.

\* Male records represented 67.57%.

\* Female records represented 32.43%.

\* Female high-income rate was 11.37%.

\* Male high-income rate was 31.38%.

\* Overall accuracy was 84.68%.

\* Overall precision was 73.72%.

\* Overall recall was 59.78%.

\* Group performance differed between male and female records.



\### Assumptions or interpretations



The following are risk interpretations rather than direct proof:



\* Historical patterns may contribute to observed demographic differences.

\* The dataset may not represent current populations.

\* Underrepresented groups may have less reliable estimates.

\* Deployment in high-impact decisions could create significant harm.

\* Sensitive attributes may act as proxies for other socioeconomic characteristics.



These assumptions require additional domain-specific research before making causal claims.



\---



\## 13. Mitigation Plan



Before deployment, the following actions should be applied.



\### 1. Improve data representativeness



Evaluate whether the training data represents the intended deployment population across relevant demographic groups.



\### 2. Measure subgroup performance



Report accuracy, precision, recall, false-positive rates, and false-negative rates separately for relevant groups.



\### 3. Investigate missingness



Do not automatically remove missing records without checking whether missingness is correlated with demographic or outcome differences.



\### 4. Evaluate sensitive-feature influence



Test whether sensitive attributes or proxy variables materially influence model decisions.



\### 5. Use fairness-aware evaluation



Use multiple fairness metrics instead of relying only on aggregate accuracy.



\### 6. Add human oversight



High-impact decisions should include meaningful human review rather than relying entirely on automated predictions.



\### 7. Apply data minimization



Collect only the information required for the intended task and avoid unnecessary personal or sensitive information.



\### 8. Document model limitations



Maintain a model card describing intended use, limitations, evaluation data, subgroup results, and known risks.



\### 9. Monitor after deployment



Fairness and performance should be monitored over time because population distributions and model behavior can change.



\### 10. Provide an appeal mechanism



People affected by an automated decision should have a way to request human review and correct inaccurate information.



\---



\## 14. Risk Rating



\### Final Risk Rating: HIGH



The system receives a \*\*HIGH\*\* risk rating for potential deployment in consequential decision-making.



The rating is based on several pieces of evidence:



\* Significant demographic imbalance exists in the dataset.

\* Income labels are imbalanced.

\* High-income outcome rates differ substantially across sex and race groups.

\* Model recall differs between male and female groups.

\* Positive prediction rates differ substantially between groups.

\* The dataset contains potentially sensitive demographic and socioeconomic information.

\* The model produced a convergence warning during training.

\* The dataset may not represent a modern deployment population.



This rating does not mean that the dataset is unusable for educational research. Instead, it means that additional fairness, privacy, validation, and governance controls would be required before using a similar system for high-impact decisions.



\---



\## 15. What the Audit Can and Cannot Establish



This audit establishes measurable differences in the selected dataset and baseline model.



However, it does not establish:



\* Causality between demographic characteristics and income.

\* Intentional discrimination.

\* Real-world performance in a modern population.

\* That the model would behave identically in another dataset.

\* That removing sensitive attributes would eliminate unfairness.

\* That the observed disparities alone determine legal or regulatory violations.



Further research would be required before making those claims.



\---



\## 16. Research Question Answer



> \*\*What are the most important responsible AI risks in the chosen system, and what evidence-based mitigations should be applied before deployment?\*\*



The most important risks are \*\*demographic imbalance, unequal outcome rates, subgroup performance differences, privacy exposure, dataset limitations, and insufficient transparency\*\*.



The audit provides direct evidence of these concerns. For example, the high-income outcome rate is \*\*11.37% for females compared with 31.38% for males\*\*, while the baseline model also shows different recall and positive prediction rates between the groups.



The evidence supports applying data-quality checks, subgroup evaluation, fairness testing, privacy minimization, human oversight, transparent documentation, continuous monitoring, and appeal mechanisms before any consequential deployment.



Therefore, a model should not be considered deployment-ready simply because its overall accuracy is high. Responsible deployment requires evidence that performance and risks have been examined across affected groups and that appropriate safeguards are in place.



\---



\## 17. Sources



1\. UCI Machine Learning Repository — Adult Dataset

   https://archive.ics.uci.edu/dataset/2/adult



2\. scikit-learn Documentation — Logistic Regression

   https://scikit-learn.org/stable/modules/linear\_model.html#logistic-regression



3\. NIST — Artificial Intelligence Risk Management Framework

   https://www.nist.gov/itl/ai-risk-management-framework



4\. NIST — AI RMF Playbook

   https://airc.nist.gov/airmf-resources/playbook/



\---



\## 18. Reproducibility



The audit was implemented in Python using:



\* pandas

\* NumPy

\* scikit-learn

\* Matplotlib



The main script is `audit.py`.



Running the script downloads the public dataset, performs the audit, trains the baseline model, generates the audit results, and creates the visualization files.



Generated evidence files:



\* `audit\_results.csv`

\* `audit\_visualization\_1.png`

\* `audit\_visualization\_2.png`

\* `audit\_visualization\_3.png`



