#assignment 15

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

# Question 1: Load and Inspect the Data
# Create a DataFrame named df from customer_data.
# Print:
df = pd.DataFrame(customer_data)
# the first five rows;
print("First five rows:")
print(df.head())
# the DataFrame shape;
print("\nShape:")
print(df.shape)
# the column names;
print("\nColumn names:")
print(df.columns)
# the missing-value count for each column.
print("\nMissing values:")
print(df.isnull().sum())


# Question 2: Select the Clustering Features
# Create:
X = df[["annual_income", "spending_score"]]
# Print the first five rows of X.
print(X.head())
# In a comment, explain why customer_id should not be used as a clustering feature.
# customer_id should not be used as a clustering feature because it is only an identifier
# and does not represent any meaningful customer behavior or characteristics


# Question 3: Use the Elbow Method
# For every value of k from 1 to 7:
# create KMeans(n_clusters=k, random_state=42, n_init=10);
# train it with X;
# add its inertia_ value to a list named inertias.
# Print each k and inertia value rounded to two decimal places.
# Plot the inertia values against k using markers, axis labels, a title, and a grid. Save the chart as:
# elbow_curve.png
# Use plt.tight_layout() and plt.close() after saving.

inertias = []
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    print(f"k = {k}, Inertia = {kmeans.inertia_:.2f}")
plt.figure(figsize=(8, 5))
plt.plot(range(1, 8), inertias, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal k")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()



# Question 4: Train the Final K-Means Model
# Use three clusters:
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)
# Print the complete DataFrame and the number of customers in each cluster.
print(df)
print("\nNumber of customers in each cluster:")
print(df["cluster"].value_counts())
# Add a comment explaining why cluster numbers such as 0, 1, and 2 are identifiers rather than rankings.
# Cluster numbers (0, 1, 2) are only identifiers assigned by the algorithm.
# They do not indicate rankings, importance, or an order from low to high.




# Question 5: Inspect the Centroids
# Get the cluster centres using:
centroids = model.cluster_centers_
# Print the centroids rounded to two decimal places. Clearly label the income and spending values in your output.
print("Cluster Centroids:")
for i, centroid in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Annual Income = {centroid[0]:.2f}, "
        f"Spending Score = {centroid[1]:.2f}"
    )




# Question 6: Visualize Clusters and Centroids
# Create a scatter plot with:
# annual income on the x-axis;
# spending score on the y-axis;
# customer points coloured by cluster;
# centroids shown as large red X markers;
# a title, axis labels, colour bar, and centroid legend.
# Save it as:
# customer_clusters.png
# Use plt.tight_layout() and plt.close() after saving.

plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=60
)
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    marker="X",
    s=250,
    label="Centroids"
)
plt.title("Customer Segments using K-Means Clustering")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.colorbar(scatter, label="Cluster")
plt.legend()
plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()




# Question 7: Calculate the Silhouette Score
# Calculate:
score = silhouette_score(X, df["cluster"])
# Print the score rounded to three decimal places.
print(f"Silhouette Score: {score:.3f}")
# In a comment, explain that a higher silhouette score generally means points are closer to their own cluster and farther from other clusters.
# A higher silhouette score generally indicates that data points are
# closer to their own cluster and farther away from points in other clusters,
# suggesting better-defined and more distinct clusters.




# Question 8: Produce Business Insights
# Group the DataFrame by cluster and calculate the average annual income and spending score for each cluster.
cluster_summary = (
    df.groupby("cluster")[["annual_income", "spending_score"]]
      .mean()
      .round(2)
)
# Print the summary table, then identify:
print("Cluster Summary:")
print(cluster_summary)
# the cluster with the highest average spending score;
# the cluster with the highest average income;
# a cluster that could receive discount offers;
# a cluster that could receive premium-membership offers.
highest_spending_cluster = cluster_summary["spending_score"].idxmax()
highest_income_cluster = cluster_summary["annual_income"].idxmax()
discount_cluster = cluster_summary["spending_score"].idxmin()
premium_cluster = highest_income_cluster
# Print one short reason for each marketing choice. Derive the cluster numbers from the summary instead of assuming a fixed label
print(f"\nCluster with the highest average spending score: {highest_spending_cluster}")
print("Reason: These customers already spend the most and are highly engaged.")
print(f"\nCluster with the highest average income: {highest_income_cluster}")
print("Reason: These customers have the greatest purchasing power.")
print(f"\nCluster to receive discount offers: {discount_cluster}")
print("Reason: This group has the lowest average spending score, so discounts may encourage more purchases.")
print(f"\nCluster to receive premium-membership offers: {premium_cluster}")
print("Reason: This group has the highest average income and is more likely to value premium services.")



# Question 9: Export the Model
# Save the trained model:
joblib.dump(model, "kmeans_model.pkl")
# Print:
# Model saved as kmeans_model.pkl
print("Model saved as kmeans_model.pkl")
