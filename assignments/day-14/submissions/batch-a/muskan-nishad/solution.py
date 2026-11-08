# Completed during maintainer review of an empty submission.
import numpy as np

customers = np.array([[15,20],[80,85],[45,50],[18,25],[75,90],[48,45]])
print(customers, customers.shape, len(customers), sep="\n")
# No target labels are supplied; groups are discovered from the features.
group = np.array([[20,30],[30,40],[40,50]])
print("Centroid:", group.mean(axis=0))
centroid_a = np.array([20,20])
centroid_b = np.array([80,85])
customer_p = np.array([18,25])
print(centroid_a, centroid_b, customer_p, sep="\n")
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a-b)**2))
distance_a = euclidean_distance(customer_p, centroid_a)
distance_b = euclidean_distance(customer_p, centroid_b)
print(round(distance_a,2), round(distance_b,2))
if distance_a < distance_b:
    print("Customer P belongs to Cluster A")
else:
    print("Customer P belongs to Cluster B")
cluster_a, cluster_b = [], []
for customer in customers:
    if euclidean_distance(customer,centroid_a) < euclidean_distance(customer,centroid_b):
        cluster_a.append(customer)
    else:
        cluster_b.append(customer)
cluster_a, cluster_b = np.array(cluster_a), np.array(cluster_b)
print(cluster_a, cluster_b, sep="\n")
print("New centroid A:", np.round(cluster_a.mean(axis=0),2))
print("New centroid B:", np.round(cluster_b.mean(axis=0),2))
# Find the nearest centroid, assign points, average each group, move centroids,
# and repeat until assignments stop changing.
print("Several rounds may be needed because moving centroids can change the nearest group.")
