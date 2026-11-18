
# K-Means Clustering using Python

import math
import random

# Dataset
data = [
    [2, 3],
    [3, 4],
    [4, 3],
    [10, 11],
    [11, 12],
    [12, 11]
]

# Number of clusters
k = 2

# Initialize centroids
centroids = [
    [2, 3],
    [10, 11]
]

# Calculate Euclidean distance
def distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )

# K-Means algorithm
for iteration in range(10):

    clusters = [[] for _ in range(k)]

    # Assign data points to nearest centroid
    for point in data:
        distances = [
            distance(point, centroid)
            for centroid in centroids
        ]

        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)

    # Update centroids
    new_centroids = []

    for cluster in clusters:
        if cluster:
            x = sum(point[0] for point in cluster) / len(cluster)
            y = sum(point[1] for point in cluster) / len(cluster)
            new_centroids.append([x, y])
        else:
            new_centroids.append(centroids[len(new_centroids)])

    # Check convergence
    if new_centroids == centroids:
        break

    centroids = new_centroids

# Display results
print("===== K-MEANS CLUSTERING =====")

for i, cluster in enumerate(clusters):
    print("\nCluster", i + 1, ":")
    for point in cluster:
        print(point)

print("\nFinal Centroids:")
for centroid in centroids:
    print(centroid)

print("\nClustering Completed Successfully!")
