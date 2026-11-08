import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# Question 1: Load and Inspect the Data

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

df = pd.DataFrame(customer_data)

print("First five rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())


# Question 2: Select the Clustering Features

X = df[["annual_income", "spending_score"]]

print("\nFirst five rows of X:")
print(X.head())

# customer_id should not be used as a clustering feature because it is
# only an identifier and does not represent customer behaviour or characteristics.


# Question 3: Use the Elbow Method

inertias = []

for k in range(1, 8):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

    print(f"k={k}, Inertia={kmeans.inertia_:.2f}")


plt.figure()
plt.plot(range(1, 8), inertias, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid()
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()


# Question 4: Train the Final K-Means Model

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["cluster"] = model.fit_predict(X)

print("\nComplete DataFrame with clusters:")
print(df)

print("\nNumber of customers in each cluster:")
print(df["cluster"].value_counts().sort_index())

# Cluster numbers such as 0, 1, and 2 are identifiers rather than rankings.
# Cluster 2 is not automatically better than Cluster 1 or Cluster 0.


# Question 5: Inspect the Centroids

centroids = model.cluster_centers_

print("\nCentroids:")
for cluster_number, centroid in enumerate(centroids):
    print(
        f"Cluster {cluster_number}: "
        f"Income = {centroid[0]:.2f}, "
        f"Spending Score = {centroid[1]:.2f}"
    )


# Question 6: Visualize Clusters and Centroids

plt.figure()

scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    cmap="viridis",
    s=80
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    marker="X",
    s=250,
    label="Centroids"
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

# A higher silhouette score generally means that points are closer to
# their own cluster and farther from other clusters.


# Question 8: Produce Business Insights

summary = df.groupby("cluster")[
    ["annual_income", "spending_score"]
].mean()

print("\nCluster Summary:")
print(summary.round(2))


highest_spending_cluster = summary["spending_score"].idxmax()
highest_income_cluster = summary["annual_income"].idxmax()

lowest_spending_cluster = summary["spending_score"].idxmin()
lowest_income_cluster = summary["annual_income"].idxmin()


print(
    f"\nHighest average spending score: "
    f"Cluster {highest_spending_cluster}"
)

print(
    f"Highest average income: "
    f"Cluster {highest_income_cluster}"
)


# Discount offers can be targeted at the cluster with the lowest
# average spending score because customers may need incentives.
print(
    f"Discount offers: Cluster {lowest_spending_cluster} "
    f"because it has the lowest average spending score."
)


# Premium membership can be targeted at the cluster with the highest
# average income because these customers may have greater purchasing power.
print(
    f"Premium-membership offers: Cluster {highest_income_cluster} "
    f"because it has the highest average income."
)


# Question 9: Export the Model

joblib.dump(model, "kmeans_model.pkl")

print("\nModel saved as kmeans_model.pkl")