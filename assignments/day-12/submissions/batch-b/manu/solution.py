# Day-12: Machine Learning Fundamentals


# Question 1: Main Types of Machine Learning

# Supervised learning uses labelled data to learn the relationship
# between input features and known output labels.
print("Supervised learning: It learns from labelled data to predict outputs.")

# Unsupervised learning finds hidden patterns or groups in data
# without predefined labels.
print("Unsupervised learning: It finds patterns or groups in unlabeled data.")

# Reinforcement learning learns by interacting with an environment
# using rewards and penalties to improve decisions.
print("Reinforcement learning: It learns through rewards and penalties.")


# Question 2: Supervised or Unsupervised?

# Predicting a new house's price from previously sold houses
print("1. House price prediction: Supervised learning")

# Grouping customers without predefined labels
print("2. Customer grouping: Unsupervised learning")

# Detecting spam using labelled emails
print("3. Spam detection: Supervised learning")

# Grouping news articles without topic labels
print("4. News article grouping: Unsupervised learning")


# Question 3: Regression or Classification?

# Predicting a numerical temperature value
print("1. Tomorrow's temperature prediction: Regression")

# Predicting one of two categories: pass or fail
print("2. Student pass or fail prediction: Classification")

# Predicting a numerical bike price
print("3. Second-hand bike price prediction: Regression")

# Predicting one of two categories: cat or dog
print("4. Cat or dog image identification: Classification")


# Question 4: Loan Application

# The model learns from previous loan applications with known outcomes.
print("Learning type: Supervised learning")

# Approved and rejected are two categories.
print("Problem type: Classification")

# Explanation: The model uses labelled previous loan data to predict
# whether a new loan application should be approved or rejected.
print("Explanation: It is supervised classification because the model learns from labelled loan outcomes and predicts approved or rejected.")


# Question 5: Customer Segmentation

# The company wants to discover groups without predefined labels.
print("Learning type: Unsupervised learning")

# The task is grouping customers into different segments.
print("Problem type: Clustering")

# Explanation: Labels are not required because the algorithm discovers
# natural groups from the customer data.
print("Explanation: Labels are not required because the algorithm discovers natural customer groups from the available data.")


# Question 6: Reinforcement Learning

# A robot receives a reward for correct movement and a penalty for falling.
print("Reinforcement learning: A robot learns by receiving a reward for correct movement and a penalty for falling, so it improves its actions through experience.")


# Question 7: Training and Prediction

# fit() is like studying from examples and learning patterns before an exam.
print("fit(): It is like studying from examples and learning patterns before an exam.")

# predict() is like using what was learned to answer questions in the exam.
print("predict(): It is like using the knowledge learned during study to answer new exam questions.")


# Question 8: Underfitting and Overfitting

# Model A has low training and testing accuracy, so it has not learned
# the data patterns properly.
print("Model A: Underfit - Training and testing accuracy are both low.")

# Model B has good and similar training and testing accuracy,
# so it generalizes well.
print("Model B: Right fit - Training and testing accuracy are both good and similar.")

# Model C has very high training accuracy but much lower testing accuracy,
# meaning it memorized the training data.
print("Model C: Overfit - Training accuracy is very high but testing accuracy is much lower.")