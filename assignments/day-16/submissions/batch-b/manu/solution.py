import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Question 1: Download and Load the Dataset

dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")

print("Dataset path:")
print(dataset_path)

df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")

print("\nFirst five rows:")
print(df.head())

print("\nDataFrame shape:")
print(df.shape)


# Question 2: Explore the Dataset

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nDescriptive statistics:")
print(df.describe())

print("\nMissing-value count:")
print(df.isnull().sum())

print("\nSurvival counts:")
print(df["Survived"].value_counts())

# Prediction label is Survived.
# This is a binary-classification problem because Survived has
# two possible classes: 0 (Not Survived) and 1 (Survived).


# Question 3: Create an EDA Figure

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Survival counts
df["Survived"].value_counts().sort_index().plot(
    kind="bar",
    ax=axes[0, 0]
)

axes[0, 0].set_title("Survival Counts")
axes[0, 0].set_xlabel("Survived")
axes[0, 0].set_ylabel("Number of Passengers")


# 2. Average survival rate by Sex
df.groupby("Sex")["Survived"].mean().plot(
    kind="bar",
    ax=axes[0, 1]
)

axes[0, 1].set_title("Average Survival Rate by Sex")
axes[0, 1].set_xlabel("Sex")
axes[0, 1].set_ylabel("Average Survival Rate")


# 3. Average survival rate by Pclass
df.groupby("Pclass")["Survived"].mean().plot(
    kind="bar",
    ax=axes[1, 0]
)

axes[1, 0].set_title("Average Survival Rate by Pclass")
axes[1, 0].set_xlabel("Passenger Class")
axes[1, 0].set_ylabel("Average Survival Rate")


# 4. Passenger age histogram
axes[1, 1].hist(
    df["Age"].dropna(),
    bins=20
)

axes[1, 1].set_title("Passenger Age Distribution")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Number of Passengers")


plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()


# Question 4: Prepare the Data

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


# Fill missing Age values with median
data["Age"] = data["Age"].fillna(data["Age"].median())

# Fill missing Embarked values with mode
data["Embarked"] = data["Embarked"].fillna(
    data["Embarked"].mode()[0]
)

# Map Sex values
data["Sex"] = data["Sex"].map({
    "male": 0,
    "female": 1,
})

# Map Embarked values
data["Embarked"] = data["Embarked"].map({
    "S": 0,
    "C": 1,
    "Q": 2,
})


print("\nMissing values after preprocessing:")
print(data.isnull().sum())

print("\nData types after preprocessing:")
print(data.dtypes)


# Question 5: Select Features and Split the Data

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

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))

# stratify=y helps preserve similar proportions of each class
# in both the training and testing datasets.


# Question 6: Train and Evaluate a Decision Tree

decision_tree = DecisionTreeClassifier(
    random_state=42
)

decision_tree.fit(X_train, y_train)

decision_tree_predictions = decision_tree.predict(X_test)

decision_tree_accuracy = accuracy_score(
    y_test,
    decision_tree_predictions
)

print("\nDecision Tree Results:")
print("Accuracy:", round(decision_tree_accuracy, 3))

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        decision_tree_predictions
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        decision_tree_predictions
    )
)


# Question 7: Train and Evaluate a Random Forest

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

random_forest.fit(X_train, y_train)

random_forest_predictions = random_forest.predict(X_test)

random_forest_accuracy = accuracy_score(
    y_test,
    random_forest_predictions
)

print("\nRandom Forest Results:")
print("Accuracy:", round(random_forest_accuracy, 3))

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        random_forest_predictions
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        random_forest_predictions
    )
)


# Question 8: Compare the Models

model_comparison = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "Random Forest",
    ],
    "Accuracy": [
        decision_tree_accuracy,
        random_forest_accuracy,
    ],
})

print("\nModel Comparison:")
print(model_comparison)

plt.figure(figsize=(8, 5))

plt.bar(
    model_comparison["Model"],
    model_comparison["Accuracy"]
)

plt.ylim(0, 1)

plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")

plt.tight_layout()
plt.savefig("model_accuracy.png")
plt.close()


if decision_tree_accuracy > random_forest_accuracy:
    print("\nHigher test accuracy: Decision Tree")
elif random_forest_accuracy > decision_tree_accuracy:
    print("\nHigher test accuracy: Random Forest")
else:
    print("\nThe models are tied.")


# Question 9: Analyze Feature Importance

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_,
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)

plt.figure(figsize=(8, 5))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")

plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()


# Question 10: Predict a New Passenger

new_passenger = pd.DataFrame({
    "Pclass": [3],
    "Sex": [0],
    "Age": [25],
    "SibSp": [1],
    "Parch": [0],
    "Fare": [8.0],
    "Embarked": [0],
})

prediction = random_forest.predict(new_passenger)[0]

probabilities = random_forest.predict_proba(
    new_passenger
)[0]

probability_not_surviving = probabilities[0]
probability_surviving = probabilities[1]

if prediction == 1:
    print("\nPrediction: Survived")
else:
    print("\nPrediction: Not Survived")

print(
    "Probability of not surviving:",
    round(probability_not_surviving, 3)
)

print(
    "Probability of surviving:",
    round(probability_surviving, 3)
)

# A model probability is an estimate based on learned patterns,
# not a guarantee of the actual outcome.