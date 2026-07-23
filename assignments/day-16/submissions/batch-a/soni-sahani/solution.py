#assignment 16

#Start your program with:

import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Question 1: Download and Load the Dataset
# Download and load the public dataset:
dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
# Print:
# the dataset path;
print("Dataset Path:")
print(dataset_path)
# the first five rows;
print("\nFirst Five Rows:")
print(df.head())
# the DataFrame shape.
print("\nDataFrame Shape:")
print(df.shape)



# Question 2: Explore the Dataset
# Print:
# the column names;
print("Column Names:")
print(df.columns)
# eacprint("\nData Types:")
print("\nData Types:")
print(df.dtypes)
# descriptive statistics;
print("\nDescriptive Statistics:")
print(df.describe(include="all"))
# the missing-value count for every column;
print("\nMissing Values:")
print(df.isnull().sum())
# the survival counts from df["Survived"].value_counts().
print("\nSurvival Counts:")
print(df["Survived"].value_counts())
# In comments, identify the prediction label and state why this is a binary-classification problem.
# Prediction label:
# The prediction label (target variable) is "Survived".
# This is a binary-classification problem because the target variable
# has only two possible classes:
#   0 = Did not survive
#   1 = Survived
# The goal is to predict which of these two outcomes applies to each passenger.



# Question 3: Create an EDA Figure
# Create one figure containing four subplots:
plt.figure(figsize=(12, 10))
# survival counts as a bar chart;
plt.subplot(2, 2, 1)
survival_counts = df["Survived"].value_counts().sort_index()
plt.bar(survival_counts.index.astype(str), survival_counts.values, color=["red", "green"])
plt.title("Survival Counts")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
# average survival rate by Sex;
plt.subplot(2, 2, 2)
sex_survival = df.groupby("Sex")["Survived"].mean()
plt.bar(sex_survival.index, sex_survival.values, color=["skyblue", "orange"])
plt.title("Average Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Survival Rate")
# average survival rate by Pclass;
plt.subplot(2, 2, 3)
pclass_survival = df.groupby("Pclass")["Survived"].mean()
plt.bar(pclass_survival.index.astype(str), pclass_survival.values, color="purple")
plt.title("Average Survival Rate by Pclass")
plt.xlabel("Passenger Class")
plt.ylabel("Average Survival Rate")
# passenger age as a histogram with 20 bins.
plt.subplot(2, 2, 4)
plt.hist(df["Age"].dropna(), bins=20, color="steelblue", edgecolor="black")
plt.title("Passenger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
# Give every subplot a title and axis labels. Save the complete figure as:
# titanic_eda.png
# Use plt.tight_layout() and plt.close() after saving.
plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()




# Question 4: Prepare the Data
# Create an independent copy with only these columns:
data = df[
    ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
].copy()
# Then:
# fill missing Age values with the median age;
data["Age"] = data["Age"].fillna(data["Age"].median())
# fill missing Embarked values with its mode;
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])
# map Sex using {"male": 0, "female": 1};
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
# map Embarked using {"S": 0, "C": 1, "Q": 2}.
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})
# Print the missing-value counts and data types after preprocessing. The final feature data must contain no missing or text values.
print("Missing Values After Preprocessing:")
print(data.isnull().sum())
print("\nData Types After Preprocessing:")
print(data.dtypes)



# Question 5: Select Features and Split the Data
# Create:
X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = data["Survived"]
#Split the data:
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
# Print the number of training and testing rows. Explain in a comment why stratify=y helps preserve the class proportions.
print("Number of Training Rows:", X_train.shape[0])
print("Number of Testing Rows:", X_test.shape[0])
# The stratify=y parameter ensures that the proportion of each class (Survived = 0 and Survived = 1) is maintained in both the training
# and testing datasets. This helps create representative datasets and improves the reliability of model evaluation.



# Question 6: Train and Evaluate a Decision Tree
# Train:
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)
# Predict the test data and print:
y_pred_dt = decision_tree.predict(X_test)
# accuracy rounded to three decimal places;
accuracy = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Accuracy: {accuracy:.3f}")
# the confusion matrix;
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_dt))
# the classification report.
print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt))




# Question 7: Train and Evaluate a Random Forest
# Train:
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)
random_forest.fit(X_train, y_train)
# Predict the test data and print the same three evaluation results as Question 6.
y_pred_rf = random_forest.predict(X_test)
# Print the accuracy (rounded to three decimal places)
accuracy = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {accuracy:.3f}")
# Print the confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))
# Print the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_rf))



# Question 8: Compare the Models
# Create and print a DataFrame with two columns:
results = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [
        accuracy_score(y_test, y_pred_dt),
        accuracy_score(y_test, y_pred_rf)
    ]
})
print(results)
# Model
# Accuracy
# It must contain one row for the Decision Tree and one for the Random Forest.
# Plot their accuracies as a bar chart with a y-axis range from 0 to 1. Save it as:
# model_accuracy.png
# Print the name of the model with the higher test accuracy. If the accuracies are equal, print that they are tied.
plt.figure(figsize=(6, 4))
plt.bar(results["Model"], results["Accuracy"], color=["skyblue", "lightgreen"])
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.savefig("model_accuracy.png")
plt.close()
dt_accuracy = accuracy_score(y_test, y_pred_dt)
rf_accuracy = accuracy_score(y_test, y_pred_rf)

if dt_accuracy > rf_accuracy:
    print("\nThe model with the higher test accuracy is: Decision Tree")
elif rf_accuracy > dt_accuracy:
    print("\nThe model with the higher test accuracy is: Random Forest")
else:
    print("\nThe Decision Tree and Random Forest are tied in test accuracy.")



# Question 9: Analyze Feature Importance
# Create a DataFrame containing each feature and its importance from:
# random_forest.feature_importances_
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest.feature_importances_
})
# Sort it from highest to lowest and print it.
feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)
print(feature_importance)
# Create a bar chart of the sorted values and save it as:
# feature_importance.png
plt.figure(figsize=(8, 5))
plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"],
    color="steelblue"
)
plt.title("Random Forest Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()


# Question 10: Predict a New Passenger
# Use:
new_passenger = pd.DataFrame({
    "Pclass": [3],
    "Sex": [0],
    "Age": [25],
    "SibSp": [1],
    "Parch": [0],
    "Fare": [8.0],
    "Embarked": [0],
})
# Use the Random Forest to print:
# Survived or Not Survived;
# the probability of not surviving;
# the probability of surviving.
# Round both probabilities to three decimal places. Add a comment explaining that a model probability is an estimate, not a guarantee.
prediction = random_forest.predict(new_passenger)[0]
probabilities = random_forest.predict_proba(new_passenger)[0]
if prediction == 1:
    print("Prediction: Survived")
else:
    print("Prediction: Not Survived")
print(f"Probability of Not Surviving: {probabilities[0]:.3f}")
print(f"Probability of Surviving: {probabilities[1]:.3f}")
# The predicted probabilities are estimates produced by the model based
# on patterns learned from the training data. They indicate the model's
# confidence but do not guarantee that the predicted outcome will occur.



