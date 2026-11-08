## Topic: Titanic Classification Project

import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ==========================================================
# Question 1: Download and Load the Dataset
# ==========================================================

dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")

print("Dataset Path:")
print(dataset_path)

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# ==========================================================
# Question 2: Explore the Dataset
# ==========================================================

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDescriptive Statistics:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSurvival Counts:")
print(df["Survived"].value_counts())

# Prediction label: Survived
# This is a binary classification problem because the target
# variable has only two classes:
# 0 = Not Survived
# 1 = Survived

# ==========================================================
# Question 3: Create EDA Figure
# ==========================================================

plt.figure(figsize=(12, 10))

# Survival Counts
plt.subplot(2, 2, 1)
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Counts")
plt.xlabel("Survived")
plt.ylabel("Count")

# Survival Rate by Sex
plt.subplot(2, 2, 2)
df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Average Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Survival Rate")

# Survival Rate by Pclass
plt.subplot(2, 2, 3)
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Average Survival Rate by Pclass")
plt.xlabel("Passenger Class")
plt.ylabel("Average Survival Rate")

# Age Histogram
plt.subplot(2, 2, 4)
plt.hist(df["Age"].dropna(), bins=20)
plt.title("Passenger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()

# ==========================================================
# Question 4: Prepare the Data
# ==========================================================

data = df[
    ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
].copy()

# Fill missing values
data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

# Encode categorical values
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})

print("\nMissing Values After Preprocessing:")
print(data.isnull().sum())

print("\nData Types After Preprocessing:")
print(data.dtypes)

# ==========================================================
# Question 5: Feature Selection and Train-Test Split
# ==========================================================

X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("\nTraining Rows:", len(X_train))
print("Testing Rows:", len(X_test))

# stratify=y ensures that the proportion of survived and
# not survived passengers remains approximately the same
# in both the training and testing datasets.

# ==========================================================
# Question 6: Decision Tree
# ==========================================================

decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

dt_predictions = decision_tree.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_predictions)

print("\nDecision Tree Accuracy:")
print(round(dt_accuracy, 3))

print("\nDecision Tree Confusion Matrix:")
print(confusion_matrix(y_test, dt_predictions))

print("\nDecision Tree Classification Report:")
print(classification_report(y_test, dt_predictions))

# ==========================================================
# Question 7: Random Forest
# ==========================================================

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

random_forest.fit(X_train, y_train)

rf_predictions = random_forest.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_predictions)

print("\nRandom Forest Accuracy:")
print(round(rf_accuracy, 3))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, rf_predictions))

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_predictions))

# ==========================================================
# Question 8: Compare Models
# ==========================================================

comparison = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [dt_accuracy, rf_accuracy]
})

print("\nModel Comparison:")
print(comparison)

plt.figure(figsize=(6, 4))
plt.bar(comparison["Model"], comparison["Accuracy"])
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.savefig("model_accuracy.png")
plt.close()

if rf_accuracy > dt_accuracy:
    print("\nBest Model: Random Forest")
elif dt_accuracy > rf_accuracy:
    print("\nBest Model: Decision Tree")
else:
    print("\nBoth models are tied.")

# ==========================================================
# Question 9: Feature Importance
# ==========================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_
})

importance = importance.sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(importance)

plt.figure(figsize=(8, 5))
plt.bar(importance["Feature"], importance["Importance"])
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

# ==========================================================
# Question 10: Predict New Passenger
# ==========================================================

new_passenger = pd.DataFrame({
    "Pclass": [3],
    "Sex": [0],
    "Age": [25],
    "SibSp": [1],
    "Parch": [0],
    "Fare": [8.0],
    "Embarked": [0],
})

prediction = random_forest.predict(new_passenger)
probability = random_forest.predict_proba(new_passenger)

print("\nPrediction for New Passenger:")

if prediction[0] == 1:
    print("Survived")
else:
    print("Not Survived")

print("Probability of Not Surviving:", round(probability[0][0], 3))
print("Probability of Surviving:", round(probability[0][1], 3))

# Model probabilities are estimates based on learned patterns.
# They indicate likelihoods, not guaranteed outcomes.