# python3 -m pip install kagglehub pandas matplotlib scikit-learn

import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ### Question 1: Download and Load the Dataset
# Download and load the public dataset:
dataset_path = kagglehub.dataset_download("yasserh/titanic-dataset")
df = pd.read_csv(dataset_path + "/Titanic-Dataset.csv")
# Print:
# 1. the dataset path;
print(dataset_path)
# 2. the first five rows;
print(df.head(5))
# 3. the DataFrame shape.
print(df.shape)


# ### Question 2: Explore the Dataset
# Print:
# 1. the column names;
print(df.columns)
# 2. each column's data type;
print(df.dtypes)
# 3. descriptive statistics;
print(df.describe())
# 4. the missing-value count for every column;
print(df.isnull().sum())
# 5. the survival counts from `df["Survived"].value_counts()`.
print(df["Survived"].value_counts())

# In comments, identify the prediction label and state why this is a binary-classification problem.
# Prediction Label = Survived
# This is a binary classification problem because there are onlytwo possible outcomes:
# 0 = Not Survived
# 1 = Survived


# ### Question 3: Create an EDA Figure
plt.figure(figsize = (12, 10))
# Create one figure containing four subplots:

# 1. survival counts as a bar chart;
plt.subplot(2,2,1)
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")

# 2. average survival rate by `Sex`;
plt.subplot(2,2,2)
df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Average Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Survival")

# 3. average survival rate by `Pclass`;
plt.subplot(2,2,3)
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Average Survival Rate by Pclass")
plt.xlabel("Passanger Class")
plt.ylabel("Average Survival")

# 4. passenger age as a histogram with 20 bins.
plt.subplot(2,2,4)
plt.hist(df["Age"].dropna(),bins = 20)
plt.title("Passanger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Give every subplot a title and axis labels. Save the complete figure as:

# ```text
# titanic_eda.png
# ```
# Use `plt.tight_layout()` and `plt.close()` after saving.
plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.close()



# ### Question 4: Prepare the Data
# Create an independent copy with only these columns:
data = df[
    ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
].copy()
# Then:
# 1. fill missing `Age` values with the median age;
data["Age"] = data["Age"].fillna(data["Age"].median())
# 2. fill missing `Embarked` values with its mode;
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])
# 3. map `Sex` using `{"male": 0, "female": 1}`;
data["Sex"] = data["Sex"].map({ "male": 0, "female": 1,})
# 4. map `Embarked` using `{"S": 0, "C": 1, "Q": 2}`.
data["Embarked"] = data["Embarked"].map({"S": 0,"C": 1,"Q": 2, })

# Print the missing-value counts and data types after preprocessing. The final feature data must contain no missing or text values.
print(data.isnull().sum())
print(data.dtypes)


# ### Question 5: Select Features and Split the Data
# Create:
X = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = data["Survived"]

# Split the data:
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
# Print the number of training and testing rows. Explain in a comment why `stratify=y` helps preserve the class proportions.
print(f"Number of Training: {len(X_train)} and Testing rows: {len(X_test)}")
# stratify=y, preserve the properties the propotion of survived and not survived passengers in both training and testing data.


# ### Question 6: Train and Evaluate a Decision Tree
# Train:
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)
dt_prediction = decision_tree.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_prediction)
# Predict the test data and print:
# 1. accuracy rounded to three decimal places;
print(f"Accuracy: {dt_accuracy:.3f}")
# 2. the confusion matrix;
print(f"Confusion Matrix:\n {confusion_matrix(y_test, dt_prediction)}")
# 3. the classification report.
print(f"Classification Report:\n{classification_report(y_test, dt_prediction)}")


# ### Question 7: Train and Evaluate a Random Forest
# Train:
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)
random_forest.fit(X_train, y_train)
rf_prediction = random_forest.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_prediction)
# Predict the test data and print the same three evaluation results as Question 6.
print(f"Accuracy: {rf_accuracy:.3f}")
print(f"Confusion Matrix:\n {confusion_matrix(y_test, rf_prediction)}")
print(f"Classification Report:\n{classification_report(y_test, rf_prediction)}")


# ### Question 8: Compare the Models
# Create and print a DataFrame with two columns:
# Model
# Accuracy
comparison = pd.DataFrame(
    {
        "Model": ["Decision Tree", "Random Forest",],
        "Accuracy": [dt_accuracy, rf_accuracy,],
    }
)
print(f"Model Comparison: {comparison}")
# It must contain one row for the Decision Tree and one for the Random Forest.
# Plot their accuracies as a bar chart with a y-axis range from `0` to `1`. Save it as:
plt.figure(figsize=(6, 5))
plt.bar(comparison["Model"],comparison["Accuracy"],)
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.savefig("model_accuracy.png")
plt.close()

# Print the name of the model with the higher test accuracy. If the accuracies are equal, print that they are tied.
if rf_accuracy > dt_accuracy:
    print("High Accuracy Model: Random Forest")

elif dt_accuracy > rf_accuracy:
    print("High Accuracy Model: Decision Tree")

else:
    print("Both models have equal accuracy.")



# ### Question 9: Analyze Feature Importance
# Create a DataFrame containing each feature and its importance from:
# random_forest.feature_importances_
importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": random_forest.feature_importances_,
    }
)
# Sort it from highest to lowest and print it.
importance = importance.sort_values(
    by="Importance",
    ascending=False,
)
print(f"Feature Importance: {importance}")

# Create a bar chart of the sorted values and save it as:
plt.figure(figsize=(8, 5))
plt.bar(
    importance["Feature"],
    importance["Importance"],
)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()


# ### Question 10: Predict a New Passenger
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
prediction = random_forest.predict(new_passenger)
probability = random_forest.predict_proba(new_passenger)
# Use the Random Forest to print:
# 1. `Survived` or `Not Survived`;
if prediction[0] == 1:
    print("Prediction: Survived")
else:
    print("Prediction: Not Survived")
# 2. the probability of not surviving;
print(f"Probability of Not Surviving: {probability[0][0]:.3f}")
# 3. the probability of surviving.
print(f"Probability of Surviving: {probability[0][1]:.3f}")

# Round both probabilities to three decimal places. Add a comment explaining that a model probability is an estimate, not a guarantee.
# Model probabilities are estimates based on the learned data. They indicate likelihood, not a guaranteed outcome.
