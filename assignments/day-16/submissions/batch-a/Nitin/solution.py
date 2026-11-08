import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# -------------------------------
# Question 1: Download and Load Dataset
# -------------------------------

dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")

print("Dataset Path:")
print(dataset_path)

print("\nFirst Five Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

# -------------------------------
# Question 2: Explore Dataset
# -------------------------------

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSurvival Counts:")
print(df["Survived"].value_counts())

# Prediction Label = Survived
# This is a binary classification problem because there are only
# two possible outputs: 0 (Not Survived) and 1 (Survived).

# -------------------------------
# Question 3: Create EDA Figure
# -------------------------------

plt.figure(figsize=(12, 8))

# Survival Count
plt.subplot(2, 2, 1)
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Counts")
plt.xlabel("Survived")
plt.ylabel("Count")

# Survival Rate by Sex
plt.subplot(2, 2, 2)
df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Survival")

# Survival Rate by Pclass
plt.subplot(2, 2, 3)
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Pclass")
plt.ylabel("Average Survival")

# Age Distribution
plt.subplot(2, 2, 4)
df["Age"].hist(bins=20)
plt.title("Passenger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()

print("\nEDA figure saved as titanic_eda.png")

# -------------------------------
# Question 4: Prepare Data
# -------------------------------

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

# Fill missing values
data["Age"].fillna(data["Age"].median(), inplace=True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)

# Encode categorical columns
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})

print("\nMissing Values After Preprocessing:")
print(data.isnull().sum())

print("\nData Types After Preprocessing:")
print(data.dtypes)

# -------------------------------
# Question 5: Feature Selection & Train-Test Split
# -------------------------------

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

print("\nTraining Rows:", len(X_train))
print("Testing Rows:", len(X_test))

# stratify=y keeps the proportion of survived and
# not survived passengers similar in both training
# and testing datasets.

# -------------------------------
# Question 6: Decision Tree
# -------------------------------

decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

dt_pred = decision_tree.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_pred)

print("\nDecision Tree Accuracy:", round(dt_accuracy, 3))

print("\nDecision Tree Confusion Matrix:")
print(confusion_matrix(y_test, dt_pred))

print("\nDecision Tree Classification Report:")
print(classification_report(y_test, dt_pred))


# -------------------------------
# Question 7: Random Forest
# -------------------------------

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest.fit(X_train, y_train)

rf_pred = random_forest.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred)

print("\nRandom Forest Accuracy:", round(rf_accuracy, 3))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, rf_pred))

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_pred))


# -------------------------------
# Question 8: Compare Models
# -------------------------------

comparison = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [dt_accuracy, rf_accuracy]
})

print("\nModel Comparison")
print(comparison)

plt.figure(figsize=(6,4))
plt.bar(comparison["Model"], comparison["Accuracy"])
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.ylim(0,1)
plt.tight_layout()
plt.savefig("model_accuracy.png")
plt.close()

if rf_accuracy > dt_accuracy:
    print("\nBest Model: Random Forest")
elif dt_accuracy > rf_accuracy:
    print("\nBest Model: Decision Tree")
else:
    print("\nBoth models have equal accuracy.")


# -------------------------------
# Question 9: Feature Importance
# -------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print(importance)

plt.figure(figsize=(8,5))
plt.bar(
    importance["Feature"],
    importance["Importance"]
)
plt.title("Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()


# -------------------------------
# Question 10: Predict New Passenger
# -------------------------------

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

print("\nNew Passenger Prediction")

if prediction[0] == 1:
    print("Prediction: Survived")
else:
    print("Prediction: Not Survived")

print("Probability of Not Surviving:",
      round(probability[0][0], 3))

print("Probability of Surviving:",
      round(probability[0][1], 3))

# Model probabilities are estimates, not guarantees.