import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Dataset
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
df = pd.DataFrame(customer_data)

print("First Five Rows:")
print(df.head())

print("\nDataFrame Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# Question 2: Select the Clustering Features
X = df[["annual_income", "spending_score"]]

print("\nFirst Five Rows of X:")
print(X.head())

# customer_id should not be used because it is only a unique identifier
# and does not describe customer behavior or characteristics.

# Question 3: Use the Elbow Method
inertias = []

print("\nElbow Method Results:")
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)

    inertias.append(kmeans.inertia_)

    print(f"k = {k}, Inertia = {kmeans.inertia_:.2f}")

plt.figure(figsize=(6, 4))
plt.plot(range(1, 8), inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()

# Question 4: Train the Final K-Means Model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

df["cluster"] = model.fit_predict(X)

print("\nComplete DataFrame:")
print(df)

print("\nCustomers in Each Cluster:")
print(df["cluster"].value_counts().sort_index())

# Cluster numbers like 0, 1, and 2 are identifiers only.
# They do not represent rankings or order.

# Question 5: Inspect the Centroids
centroids = model.cluster_centers_

print("\nCluster Centroids:")
for i, centroid in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Annual Income = {centroid[0]:.2f}, "
        f"Spending Score = {centroid[1]:.2f}"
    )

# Question 6: Visualize Clusters and Centroids
plt.figure(figsize=(7, 5))

scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=300,
    color="red",
    label="Centroids",
)

plt.title("Customer Clusters")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.colorbar(scatter, label="Cluster")
plt.legend()

plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()

# Question 7: Calculate the Silhouette Score
score = silhouette_score(X, df["cluster"])

print(f"\nSilhouette Score: {score:.3f}")

# A higher silhouette score generally means that points are closer
# to their own cluster and farther from other clusters.

# Question 8: Produce Business Insights
summary = df.groupby("cluster")[["annual_income", "spending_score"]].mean()

print("\nCluster Summary:")
print(summary.round(2))

highest_spending_cluster = summary["spending_score"].idxmax()
highest_income_cluster = summary["annual_income"].idxmax()
discount_cluster = summary["spending_score"].idxmin()

premium_cluster = highest_spending_cluster

print(f"\nCluster with highest average spending score: {highest_spending_cluster}")
print("Reason: Customers in this cluster spend the most.")

print(f"\nCluster with highest average income: {highest_income_cluster}")
print("Reason: Customers in this cluster have the highest income.")

print(f"\nCluster for discount offers: {discount_cluster}")
print("Reason: Customers have the lowest average spending score.")

print(f"\nCluster for premium membership offers: {premium_cluster}")
print("Reason: Customers have the highest spending score.")

# Question 9: Export the Model
joblib.dump(model, "kmeans_model.pkl")

print("\nModel saved as kmeans_model.pkl")

# K-Means Process Explanation
print("\nK-Means Explanation:")
print("1. Find the nearest centroid.")
print("2. Assign points to groups.")
print("3. Calculate each group's new average.")
print("4. Move the centroids.")
print("5. Repeat until the groups stop changing.")

print(
    "\nThe algorithm may need several rounds because centroids keep moving "
    "until the best cluster positions are found."
)