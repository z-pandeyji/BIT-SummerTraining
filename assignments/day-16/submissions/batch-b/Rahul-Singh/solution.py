import matplotlib.pyplot as plt
import pandas as pd
import kagglehub

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Question 1

dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")

df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")

print("Dataset Path:", dataset_path)
print(df.head())
print("Shape:", df.shape)

# Question 2

print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())
print(df["Survived"].value_counts())

# Label = Survived
# This is a binary classification problem because there are only two classes:
# 0 = Not Survived, 1 = Survived

# Question 3

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")

plt.subplot(2, 2, 2)
df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Survival by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Survival")

plt.subplot(2, 2, 3)
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Survival by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Survival")

plt.subplot(2, 2, 4)
df["Age"].plot(kind="hist", bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()

# Question 4

data = df[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
        "Survived",
    ]
].copy()

data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})

print(data.isnull().sum())
print(data.dtypes)

# Question 5

X = data[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
    ]
]

y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("Training Rows:", len(X_train))
print("Testing Rows:", len(X_test))

# stratify=y keeps the class distribution similar
# in both training and testing data.

# Question 6

decision_tree = DecisionTreeClassifier(random_state=42)

decision_tree.fit(X_train, y_train)

dt_pred = decision_tree.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_pred)

print("Decision Tree Accuracy:", round(dt_accuracy, 3))
print(confusion_matrix(y_test, dt_pred))
print(classification_report(y_test, dt_pred))

# Question 7

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

random_forest.fit(X_train, y_train)

rf_pred = random_forest.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred)

print("Random Forest Accuracy:", round(rf_accuracy, 3))
print(confusion_matrix(y_test, rf_pred))
print(classification_report(y_test, rf_pred))

# Question 8

comparison = pd.DataFrame(
    {
        "Model": ["Decision Tree", "Random Forest"],
        "Accuracy": [dt_accuracy, rf_accuracy],
    }
)

print(comparison)

plt.figure(figsize=(5, 4))
plt.bar(comparison["Model"], comparison["Accuracy"])
plt.ylim(0, 1)
plt.title("Model Accuracy")
plt.ylabel("Accuracy")
plt.savefig("model_accuracy.png")
plt.close()

if rf_accuracy > dt_accuracy:
    print("Best Model: Random Forest")
elif dt_accuracy > rf_accuracy:
    print("Best Model: Decision Tree")
else:
    print("Both models are tied.")

# Question 9

importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": random_forest.feature_importances_,
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False,
)

print(importance)

plt.figure(figsize=(7, 4))
plt.bar(importance["Feature"], importance["Importance"])
plt.title("Feature Importance")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

# Question 10

new_passenger = pd.DataFrame(
    {
        "Pclass": [3],
        "Sex": [0],
        "Age": [25],
        "SibSp": [1],
        "Parch": [0],
        "Fare": [8.0],
        "Embarked": [0],
    }
)

prediction = random_forest.predict(new_passenger)[0]

probability = random_forest.predict_proba(new_passenger)[0]

if prediction == 1:
    print("Prediction: Survived")
else:
    print("Prediction: Not Survived")

print("Probability of Not Surviving:", round(probability[0], 3))
print("Probability of Surviving:", round(probability[1], 3))

# Model probabilities are estimates, not guarantees.