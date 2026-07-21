#assignment 12

### Question 1: Main Types of Machine Learning
# Write one or two lines explaining each type:
# 1. Supervised learning
print("Supervised learning: Learns from labeled examples, e.g., predicting exam scores")
# 2. Unsupervised learning
print("Unsupervised learning: Finds hidden patterns, e.g., customer segmentation")
# 3. Reinforcement learning
print("Reinforcement learning: Learns via feedback, e.g., game-playing agents")


### Question 2: Supervised or Unsupervised?
# Write whether each task uses supervised or unsupervised learning:
# 1. Predicting a new house's price from previously sold houses
print("Predicting house price: Supervised learning")
# 2. Grouping customers by their shopping behaviour without predefined labels
print("Grouping customers: Unsupervised learning")
# 3. Detecting spam using emails already labelled `spam` or `not spam`
print("Spam detection: Supervised learning")
# 4. Grouping news articles by topic without topic labels
print("Grouping news articles: Unsupervised learning")



### Question 3: Regression or Classification?
# Identify each task as regression or classification:
# 1. Predicting tomorrow's temperature
print("Predicting temperature: Regression (continuous output)")
# 2. Predicting whether a student will pass or fail
print("Student pass/fail prediction: Classification (categorical output)")
# 3. Predicting the price of a second-hand bike
print("Bike price prediction: Regression (continuous output)")
# 4. Identifying whether an image contains a cat or a dog
print("Cat vs Dog image: Classification (categorical output)")



### Question 4: Loan Application
# A loan application uses income, credit score, age, employment type, and previous loan history to decide whether a loan should be `approved` or `rejected`.
# Print:
# - the learning type: supervised or unsupervised;
print("Learning type: Supervised learning")
# - the problem type: regression or classification;
print("Problem type: Classification")
# - one sentence explaining your answer.
print("Explanation: Loan approval is decided using labeled past data, and the outcome is categorical (approved/rejected).")



### Question 5: Customer Segmentation
# A company has customer age, city, total purchases, application usage time, and service preference. It wants to discover customer groups, but it has no labels such as `premium` or `regular`.
# Print:
# - the learning type;
print("Learning type: Unsupervised learning")
# - the problem type;
print("Problem type: Clustering")
# - one sentence explaining why labels are not required.
print("Explanation: Labels are not required because the goal is to discover natural groupings in customer data.")


### Question 6: Reinforcement Learning
# Explain why teaching a robot to walk by giving positive points for correct movement and negative points for falling is reinforcement learning.
# Include the words `reward` and `penalty` in your answer.
print("Robot walking: Reinforcement learning (reward for correct steps, penalty for falling)")


### Question 7: Training and Prediction
# In your own words, explain:
# 1. What does `fit()` do?
print("fit(): Model studies training data, like a student preparing for an exam")
# 2. What does `predict()` do?
print("predict(): Model applies learned knowledge to new data," \
      " like a student answering exam questions")
# Use the classroom comparison of studying and taking an exam.


### Question 8: Underfitting and Overfitting
# Identify each model as `underfit`, `right fit`, or `overfit`:
# Model A: Training accuracy = 50%, Testing accuracy = 48%
print("Model A: Underfit (low accuracy on both training and testing)")
# Model B: Training accuracy = 88%, Testing accuracy = 85%
print("Model B: Right fit (high accuracy and good generalization)")
# Model C: Training accuracy = 99%, Testing accuracy = 60%
print("Model C: Overfit (memorized training data, poor generalization)")





