import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


# Student data
student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}


# Question 1: Create and Inspect the DataFrame
df = pd.DataFrame(student_data)

print("Complete DataFrame:")
print(df)

print("\nFirst five rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nDescriptive Statistics:")
print(df.describe())


# Question 2: Select Features and Label
X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]

print("\nFirst five rows of X:")
print(X.head())

print("\nFirst five values of y:")
print(y.head())

# X contains the input features used to make predictions.
# y contains the target label/value that the model needs to predict.


# Question 3: Train a Linear Regression Model
model = LinearRegression()
model.fit(X, y)

print("\nLinear regression model trained")


# Question 4: Predict a New Student's Marks
new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [82],
    "previous_mark": [70]
})

predicted_mark = model.predict(new_student)

print(
    "Predicted final mark:",
    round(predicted_mark[0], 1)
)


# Question 5: Inspect Model Coefficients
print("\nModel coefficients:")
print(model.coef_)

# A coefficient shows how strongly a feature affects the prediction.
# A positive coefficient generally increases the predicted value,
# while a negative coefficient generally decreases it.


# Question 6: Create and Predict a Pass/Fail Result
df["result"] = (df["final_marks"] >= 70).astype(int)

# 1 means pass and 0 means fail.
logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X, df["result"])

predicted_result = logistic_model.predict(new_student)[0]

print("\nPredicted result number:", predicted_result)

if predicted_result == 1:
    print("Meaning: Pass")
else:
    print("Meaning: Fail")


# Question 7: Split Training and Testing Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))

# A model should be tested on data it did not use during training
# to check how well it performs on unseen data.


# Question 8: Evaluate the Regression Model
evaluation_model = LinearRegression()

evaluation_model.fit(X_train, y_train)

y_pred = evaluation_model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nActual test values:")
print(y_test.values)

print("\nPredicted values:")
print(y_pred)

print("\nMAE:", round(mae, 2))
print("R2:", round(r2, 2))

# A lower MAE is better because it means smaller prediction errors.
# An R2 value closer to 1 is better because it means the model
# explains more of the variation in the target values.