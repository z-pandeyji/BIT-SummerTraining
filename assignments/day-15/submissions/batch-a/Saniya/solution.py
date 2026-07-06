# Day 15 Assignment
#==========================================================>>>
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
#Use this dataset:
customer_data = {
    "customer_id": list(range(1, 22)),
    "annual_income": [
        15, 18, 16, 22, 19, 14, 20,
        44, 48, 46, 52, 49, 45, 50,
        78, 82, 80, 88, 85, 76, 90,
    ],
    "spending_score": [
        20, 25, 18, 30, 22, 15, 28,
        48, 52, 50, 58, 55, 46, 53,
        82, 88, 78, 90, 85, 80, 92,
    ],
}
#=========================================================>>>
## Question 1: Load and Inspect the Data
# Create a DataFrame named `df` from `customer_data`.
# 1. the first five rows;
df = pd.DataFrame(customer_data)
print("First five rows:")
print(df.head())
# 2. the DataFrame shape;
print("\nDataFrame shape:")
print(df.shape)
# 3. the column names;
print("\nColumn names:")
print(df.columns)
# 4. the missing-value count for each column.
print("\nMissing-value count for each column:")
print(df.isnull().sum())
print("="*50)
#========================================================>>>
# Question 2: Select the Clustering Features
# Create:
# X = df[["annual_income", "spending_score"]]
# Print the first five rows of `X`.
# # In a comment, explain why `customer_id` should not be used as a clustering feature.
X= df[["annual_income", "spending_score"]]
print("First five rows of X:")
print(X.head())
print("\nExplanation: 'customer_id' should not be used as a clustering feature because it is a unique identifier for each customer and does not provide any meaningful information about their behavior or characteristics. Clustering should be based on features that reflect similarities or differences among customers, such as their annual income and spending score.")      
print("="*50)
#========================================================>>>
# Question 3: Use the Elbow Method

# For every value of `k` from `1` to `7`:

# 1. create `KMeans(n_clusters=k, random_state=42, n_init=10)`;
# 2. train it with `X`;
# 3. add its `inertia_` value to a list named `inertias`.

# Print each `k` and inertia value rounded to two decimal places.

# Plot the inertia values against `k` using markers, axis labels, a title, and a grid. Save the chart as:

# ```text
# elbow_curve.png
# ```

# Use `plt.tight_layout()` and `plt.close()` after saving.
inertias = []

for k in range(1, 8):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertias.append(model.inertia_)
    print(k, round(model.inertia_, 2))
plt.plot(range(1,8), inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("K")
plt.ylabel("Inertia")
plt.grid()
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()
print("Elbow curve saved as 'elbow_curve.png'")
print("="*50)
#========================================================>>>
## Question 4: Train the Final K-Means Model

    # Use three clusters:

    # ```python
    # model = KMeans(n_clusters=3, random_state=42, n_init=10)
    # df["cluster"] = model.fit_predict(X)
    # ```

    # Print the complete DataFrame and the number of customers in each cluster.

    # Add a comment explaining why cluster numbers such as `0`, `1`, and `2` are identifiers rather than rankings.
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)
print(df)
print(df["cluster"].value_counts())
print("\nExplanation: Cluster numbers such as 0, 1, and 2 are identifiers rather than rankings because they are arbitrary labels assigned by the K-Means algorithm to differentiate between clusters. The numbers do not imply any order or hierarchy among the clusters; they simply serve as unique identifiers for each group of customers based on their characteristics.")
#========================================================>>>
## Question 5: Inspect the Centroids

    # Get the cluster centres using:

    # ```python
    # centroids = model.cluster_centers_
    # ```

    # Print the centroids rounded to two decimal places. Clearly label the income and spending values in your output.
centroids = model.cluster_centers_
for i, c in enumerate(centroids):
    print(f"Cluster {i}: Income={round(c[0],2)}, Spending={round(c[1],2)}")
#========================================================>>>
## Question 6: Visualize Clusters and Centroids

    # Create a scatter plot with:

    # - annual income on the x-axis;
    # - spending score on the y-axis;
    # - customer points coloured by cluster;
    # - centroids shown as large red `X` markers;
    # - a title, axis labels, colour bar, and centroid legend.

    # Save it as:

    # ```text
    # customer_clusters.png
    # ```

    # Use `plt.tight_layout()` and `plt.close()` after saving.
plt.scatter(df["annual_income"], df["spending_score"], c=df["cluster"])
plt.scatter(centroids[:,0], centroids[:,1], c="red", marker="X", s=200, label="Centroids")
plt.title("Customer Clusters")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.colorbar(label="Cluster")
plt.legend()
plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()
print("Customer clusters plot saved as 'customer_clusters.png'")
print("="*50)
#========================================================>>>
# Question 7: Calculate the Silhouette Score

    # Calculate:

    # ```python
    # score = silhouette_score(X, df["cluster"])
    # ```

    # Print the score rounded to three decimal places.

    # In a comment, explain that a higher silhouette score generally means points are closer to their own cluster and farther from other clusters.
score = silhouette_score(X, df["cluster"])
print("Silhouette Score:", round(score, 3))
#=========================================================>>>
## Question 8: Produce Business Insights

    # Group the DataFrame by `cluster` and calculate the average annual income and spending score for each cluster.

    # Print the summary table, then identify:

    # 1. the cluster with the highest average spending score;
    # 2. the cluster with the highest average income;
    # 3. a cluster that could receive discount offers;
    # 4. a cluster that could receive premium-membership offers.

    # Print one short reason for each marketing choice. Derive the cluster numbers from the summary instead of assuming a fixed label.
summary = df.groupby("cluster")[["annual_income","spending_score"]].mean()
print(summary)

high_spend = summary["spending_score"].idxmax()
high_income = summary["annual_income"].idxmax()
low_spend = summary["spending_score"].idxmin()
print("Highest spending cluster:", high_spend)
print("Highest income cluster:", high_income)
print("Discount offers:", low_spend, "- Low spending customers.")
print("Premium offers:", high_spend, "- High spending customers.")
print("="*50)
#========================================================>>>
    # # Question 9: Export the Model

    # Save the trained model:

    # ```python
    # joblib.dump(model, "kmeans_model.pkl")
    # ```

    # Print:

    # ```text
    # Model saved as kmeans_model.pkl
joblib.dump(model, "kmeans_model.pkl")
print("Model saved as kmeans_model.pkl")