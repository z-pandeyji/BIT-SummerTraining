\# Day 23 — Responsible AI Bias, Privacy, and Risk Audit



\## Overview



This project conducts a responsible AI audit of the \*\*UCI Adult Income Dataset\*\* and a simple logistic regression baseline classifier.



The audit focuses on four major areas:



\* Fairness

\* Privacy

\* Transparency

\* Deployment risk



The goal is to identify measurable risks and propose evidence-based mitigations before a similar system could be considered for deployment.



\---



\## Research Question



> \*\*What are the most important responsible AI risks in the chosen system, and what evidence-based mitigations should be applied before deployment?\*\*



\---



\## Dataset



The audit uses the public \*\*UCI Adult Income Dataset\*\*.



Source:



https://archive.ics.uci.edu/dataset/2/adult



The dataset contains demographic, education, employment, and financial-related attributes and a binary income target.



\### Dataset size



\* Original records: \*\*32,561\*\*

\* Records after removing missing values: \*\*30,162\*\*



\---



\## Audit Checks



The project performs the following measurable checks:



\### 1. Missing-value analysis



The script measures missing values before cleaning.



Important missing-value counts:



\* Workclass: 1,836

\* Occupation: 1,843

\* Native-country: 583



\### 2. Label imbalance



The income target distribution is measured.



\* `<=50K`: 75.11%

\* `>50K`: 24.89%



\### 3. Demographic representation



Representation is measured for sex and race.



Sex:



\* Male: 67.57%

\* Female: 32.43%



Race:



\* White: 85.98%

\* Black: 9.34%

\* Asian-Pac-Islander: 2.97%

\* Amer-Indian-Eskimo: 0.95%

\* Other: 0.77%



\### 4. Group outcome differences



High-income outcome rates are compared across demographic groups.



For sex:



\* Female: 11.37%

\* Male: 31.38%



\### 5. Model performance



A logistic regression baseline is evaluated using:



\* Accuracy

\* Precision

\* Recall



Overall results:



\* Accuracy: 84.68%

\* Precision: 73.72%

\* Recall: 59.78%



Group-level performance is also compared by sex.



\---



\## Privacy Audit



The dataset contains demographic and socioeconomic attributes that may become sensitive when combined.



A responsible AI workflow should avoid unnecessarily collecting or submitting:



\* Government identification numbers

\* Passwords

\* Authentication credentials

\* Banking information

\* Payment-card information

\* Private medical records

\* Precise residential addresses

\* Confidential employment information

\* Unrelated private documents



The project recommends data minimization and controlled access to sensitive information.



\---



\## Fairness Findings



The audit found substantial differences in demographic representation and observed outcomes.



For example, the observed high-income rate was:



| Group  | High-income rate |

| ------ | ---------------: |

| Female |           11.37% |

| Male   |           31.38% |



The baseline model also showed different subgroup results.



| Group  | Samples | Accuracy | Recall | Positive prediction rate |

| ------ | ------: | -------: | -----: | -----------------------: |

| Female |   2,446 |   91.78% | 51.88% |                    8.67% |

| Male   |   5,095 |   81.28% | 61.24% |                   25.71% |



These results demonstrate why overall accuracy alone is insufficient for responsible AI evaluation.



\---



\## Generated Files



The script generates:



```text

audit\_results.csv

audit\_visualization\_1.png

audit\_visualization\_2.png

audit\_visualization\_3.png

```



\### Visualization 1



`audit\_visualization\_1.png`



Shows the distribution of the income labels.



\### Visualization 2



`audit\_visualization\_2.png`



Shows the observed high-income outcome rate by sex.



\### Visualization 3



`audit\_visualization\_3.png`



Shows the observed high-income outcome rate by race.



\---



\## How to Run



\### 1. Activate the virtual environment



From the repository root:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



\### 2. Go to the solution directory



```powershell

cd assignments\\day-23\\submissions\\Nitin\\solution

```



\### 3. Install dependencies



```powershell

python -m pip install pandas numpy scikit-learn matplotlib

```



\### 4. Run the audit



```powershell

python audit.py

```



The script downloads the public dataset if it is not already present.



\---



\## Reproducibility



The experiment uses:



\* Python

\* pandas

\* NumPy

\* scikit-learn

\* Matplotlib



The model uses a fixed random seed of `42` for the train-test split.



The audit script automatically creates the results CSV and visualization files.



\---



\## Evidence vs Assumptions



\### Evidence-based



The following are directly measured:



\* Missing-value counts

\* Dataset size

\* Income distribution

\* Demographic representation

\* Group outcome rates

\* Overall model metrics

\* Group-level model metrics



\### Assumptions



The audit does not prove that demographic characteristics cause income differences or that the model intentionally discriminates.



Historical socioeconomic factors and dataset construction may contribute to the observed patterns.



The results should therefore be interpreted as risk evidence rather than causal proof.



\---



\## Mitigation Recommendations



Before deployment of a similar system:



1\. Validate demographic representativeness.

2\. Measure subgroup performance.

3\. Investigate missing-data patterns.

4\. Test sensitive features and proxy variables.

5\. Apply fairness-aware evaluation.

6\. Minimize collection of personal data.

7\. Add meaningful human oversight.

8\. Document model limitations.

9\. Monitor performance after deployment.

10\. Provide an appeal and correction mechanism.



\---



\## Final Risk Rating



\### HIGH



The system receives a \*\*HIGH\*\* risk rating for consequential deployment because the audit found demographic imbalance, substantial group outcome differences, subgroup model-performance differences, privacy concerns, and dataset limitations.



The project is suitable as an educational research audit, but additional validation, fairness testing, privacy controls, governance, and human oversight would be required before production use in high-impact decisions.



\---



\## Sources



\* UCI Machine Learning Repository — Adult Dataset

&#x20; https://archive.ics.uci.edu/dataset/2/adult



\* scikit-learn — Logistic Regression Documentation

&#x20; https://scikit-learn.org/stable/modules/linear\_model.html#logistic-regression



\* NIST — AI Risk Management Framework

&#x20; https://www.nist.gov/itl/ai-risk-management-framework



\* NIST — AI RMF Playbook

&#x20; https://airc.nist.gov/airmf-resources/playbook/



\---



\## Project Structure



```text

solution/

├── README.md

├── audit.py

├── report.md

├── audit\_results.csv

├── audit\_visualization\_1.png

├── audit\_visualization\_2.png

├── audit\_visualization\_3.png

└── adult.data

```



\---



\## Conclusion



This audit demonstrates that responsible AI evaluation cannot rely only on overall model accuracy.



Fairness, privacy, transparency, subgroup performance, data quality, and deployment context must all be considered before a machine learning system is used in consequential settings.



