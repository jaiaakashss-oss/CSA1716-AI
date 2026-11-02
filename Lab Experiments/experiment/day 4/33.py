
# K-Nearest Neighbours (KNN) Classification

import math
from collections import Counter

# Training dataset
# Format: [Height, Weight, Class]

training_data = [
    [150, 50, "Underweight"],
    [160, 55, "Normal"],
    [170, 65, "Normal"],
    [180, 80, "Overweight"],
    [155, 45, "Underweight"],
    [175, 75, "Overweight"],
    [165, 60, "Normal"],
    [185, 90, "Overweight"]
]

# Test data
test_data = [168, 62]

# Number of neighbours
k = 3

# Calculate Euclidean distance
def calculate_distance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2

    return math.sqrt(distance)

# KNN classification function
def knn_classify(training_data, test_data, k):

    distances = []

    for row in training_data:
        distance = calculate_distance(row[:-1], test_data)
        distances.append((distance, row[-1]))

    # Sort distances
    distances.sort(key=lambda x: x[0])

    # Select K nearest neighbours
    neighbours = distances[:k]

    print("\nNearest Neighbours:")
    for distance, label in neighbours:
        print(label, "Distance:", round(distance, 2))

    # Find majority class
    classes = [label for distance, label in neighbours]

    result = Counter(classes).most_common(1)[0][0]

    return result

# Display result
print("K-NEAREST NEIGHBOURS CLASSIFICATION")
print("-----------------------------------")

print("Test Data:", test_data)
print("K Value:", k)

prediction = knn_classify(training_data, test_data, k)

print("\nPredicted Class:", prediction)
print("\nKNN Classification Completed Successfully!")
