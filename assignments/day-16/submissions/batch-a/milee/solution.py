import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# ============================================================
# Question 1: Download and Load the Dataset
# ============================================================

dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")

print("\n" + "=" * 60)
print("QUESTION 1: DOWNLOAD AND LOAD THE DATASET")
print("=" * 60)

print("\nDataset path:")
print(dataset_path)

print("\nFirst five rows:")
print(df.head())

print("\nDataFrame shape:")
print(df.shape)


# ============================================================
# Question 2: Explore the Dataset
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 2: EXPLORE THE DATASET")
print("=" * 60)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nDescriptive statistics:")
print(df.describe())

print("\nMissing-value count for every column:")
print(df.isnull().sum())

print("\nSurvival counts:")
print(df["Survived"].value_counts())

# Prediction label:
# "Survived" is the prediction label because it is the value
# we want the machine learning models to predict.
#
# This is a binary-classification problem because Survived has
# two possible classes:
# 0 = Not Survived
# 1 = Survived


# ============================================================
# Question 3: Create an EDA Figure
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 3: CREATE EDA FIGURE")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Survival counts as a bar chart
survival_counts = df["Survived"].value_counts().sort_index()

axes[0, 0].bar(
    ["Not Survived", "Survived"],
    survival_counts.values,
)
axes[0, 0].set_title("Titanic Survival Counts")
axes[0, 0].set_xlabel("Survival Status")
axes[0, 0].set_ylabel("Number of Passengers")

# 2. Average survival rate by Sex
survival_by_sex = df.groupby("Sex")["Survived"].mean()

axes[0, 1].bar(
    survival_by_sex.index,
    survival_by_sex.values,
)
axes[0, 1].set_title("Average Survival Rate by Sex")
axes[0, 1].set_xlabel("Sex")
axes[0, 1].set_ylabel("Average Survival Rate")

# 3. Average survival rate by Pclass
survival_by_pclass = df.groupby("Pclass")["Survived"].mean()

axes[1, 0].bar(
    survival_by_pclass.index.astype(str),
    survival_by_pclass.values,
)
axes[1, 0].set_title("Average Survival Rate by Passenger Class")
axes[1, 0].set_xlabel("Passenger Class")
axes[1, 0].set_ylabel("Average Survival Rate")

# 4. Passenger age as a histogram with 20 bins
axes[1, 1].hist(
    df["Age"].dropna(),
    bins=20,
)
axes[1, 1].set_title("Passenger Age Distribution")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()

print("Saved EDA figure as titanic_eda.png")


# ============================================================
# Question 4: Prepare the Data
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 4: PREPARE THE DATA")
print("=" * 60)

data = df[
    ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
].copy()

# Fill missing Age values with the median age.
data["Age"] = data["Age"].fillna(data["Age"].median())

# Fill missing Embarked values with the mode.
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

# Map Sex to numeric values.
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# Map Embarked to numeric values.
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})

print("\nMissing-value counts after preprocessing:")
print(data.isnull().sum())

print("\nData types after preprocessing:")
print(data.dtypes)

# The final feature data contains no missing values or text values.
# Sex and Embarked have been converted from text to numeric values.


# ============================================================
# Question 5: Select Features and Split the Data
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 5: SELECT FEATURES AND SPLIT THE DATA")
print("=" * 60)

X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("\nNumber of training rows:")
print(len(X_train))

print("\nNumber of testing rows:")
print(len(X_test))

# stratify=y helps preserve approximately the same proportion of
# survived and not-survived passengers in both the training and
# testing datasets as in the original dataset.


# ============================================================
# Question 6: Train and Evaluate a Decision Tree
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 6: DECISION TREE")
print("=" * 60)

decision_tree = DecisionTreeClassifier(random_state=42)

decision_tree.fit(X_train, y_train)

decision_tree_predictions = decision_tree.predict(X_test)

decision_tree_accuracy = accuracy_score(
    y_test,
    decision_tree_predictions,
)

decision_tree_confusion_matrix = confusion_matrix(
    y_test,
    decision_tree_predictions,
)

decision_tree_classification_report = classification_report(
    y_test,
    decision_tree_predictions,
)

print("\nDecision Tree Accuracy:")
print(f"{decision_tree_accuracy:.3f}")

print("\nDecision Tree Confusion Matrix:")
print(decision_tree_confusion_matrix)

print("\nDecision Tree Classification Report:")
print(decision_tree_classification_report)


# ============================================================
# Question 7: Train and Evaluate a Random Forest
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 7: RANDOM FOREST")
print("=" * 60)

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

random_forest.fit(X_train, y_train)

random_forest_predictions = random_forest.predict(X_test)

random_forest_accuracy = accuracy_score(
    y_test,
    random_forest_predictions,
)

random_forest_confusion_matrix = confusion_matrix(
    y_test,
    random_forest_predictions,
)

random_forest_classification_report = classification_report(
    y_test,
    random_forest_predictions,
)

print("\nRandom Forest Accuracy:")
print(f"{random_forest_accuracy:.3f}")

print("\nRandom Forest Confusion Matrix:")
print(random_forest_confusion_matrix)

print("\nRandom Forest Classification Report:")
print(random_forest_classification_report)


# ============================================================
# Question 8: Compare the Models
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 8: COMPARE THE MODELS")
print("=" * 60)

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

print("\nModel comparison:")
print(model_comparison)

# Plot model accuracies.
plt.figure(figsize=(8, 6))

plt.bar(
    model_comparison["Model"],
    model_comparison["Accuracy"],
)

plt.title("Model Test Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.ylim(0, 1)

plt.tight_layout()
plt.savefig("model_accuracy.png")
plt.close()

print("\nSaved model accuracy chart as model_accuracy.png")

# Find the model with the higher test accuracy.
if decision_tree_accuracy > random_forest_accuracy:
    print("\nModel with higher test accuracy: Decision Tree")
elif random_forest_accuracy > decision_tree_accuracy:
    print("\nModel with higher test accuracy: Random Forest")
else:
    print("\nThe Decision Tree and Random Forest accuracies are tied.")


# ============================================================
# Question 9: Analyze Feature Importance
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 9: FEATURE IMPORTANCE")
print("=" * 60)

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_,
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False,
).reset_index(drop=True)

print("\nRandom Forest feature importance:")
print(feature_importance)

# Create feature importance bar chart.
plt.figure(figsize=(8, 6))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"],
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

print("\nSaved feature importance chart as feature_importance.png")


# ============================================================
# Question 10: Predict a New Passenger
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 10: PREDICT A NEW PASSENGER")
print("=" * 60)

new_passenger = pd.DataFrame({
    "Pclass": [3],
    "Sex": [0],
    "Age": [25],
    "SibSp": [1],
    "Parch": [0],
    "Fare": [8.0],
    "Embarked": [0],
})

new_prediction = random_forest.predict(new_passenger)
new_probability = random_forest.predict_proba(new_passenger)[0]

not_surviving_probability = new_probability[0]
surviving_probability = new_probability[1]

if new_prediction[0] == 1:
    prediction_label = "Survived"
else:
    prediction_label = "Not Survived"

print("\nPrediction:")
print(prediction_label)

print("\nProbability of not surviving:")
print(f"{not_surviving_probability:.3f}")

print("\nProbability of surviving:")
print(f"{surviving_probability:.3f}")

# A model probability is an estimate based on patterns learned from
# the training data; it is not a guarantee of what will happen.