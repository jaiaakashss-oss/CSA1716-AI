
# Dimensionality Reduction using PCA
# Without external libraries

import math

# Step 1: Input dataset (3 dimensions)
data = [
    [2.5, 2.4, 1.2],
    [0.5, 0.7, 0.8],
    [2.2, 2.9, 1.5],
    [1.9, 2.2, 1.1],
    [3.1, 3.0, 1.8],
    [2.3, 2.7, 1.3]
]

# Step 2: Calculate mean of each column
rows = len(data)
cols = len(data[0])

mean = [
    sum(data[i][j] for i in range(rows)) / rows
    for j in range(cols)
]

# Step 3: Center the data
centered = [
    [data[i][j] - mean[j] for j in range(cols)]
    for i in range(rows)
]

# Step 4: Calculate covariance matrix
cov = []

for i in range(cols):
    row = []
    for j in range(cols):
        value = sum(
            centered[k][i] * centered[k][j]
            for k in range(rows)
        ) / (rows - 1)
        row.append(value)
    cov.append(row)

# Step 5: Calculate eigenvectors using power iteration
def normalize(v):
    length = math.sqrt(sum(x * x for x in v))
    return [x / length for x in v]

def matrix_vector(A, v):
    return [
        sum(A[i][j] * v[j] for j in range(len(v)))
        for i in range(len(v))
    ]

def power_iteration(A):
    v = [1.0, 1.0, 1.0]

    for _ in range(1000):
        new_v = normalize(matrix_vector(A, v))
        v = new_v

    return v

# First principal component
pc1 = power_iteration(cov)

# Calculate first eigenvalue
Av = matrix_vector(cov, pc1)
eigenvalue1 = sum(pc1[i] * Av[i] for i in range(cols))

# Deflate covariance matrix
reduced_cov = [
    [
        cov[i][j] - eigenvalue1 * pc1[i] * pc1[j]
        for j in range(cols)
    ]
    for i in range(cols)
]

# Second principal component
pc2 = power_iteration(reduced_cov)

# Step 6: Project data into 2 dimensions
reduced_data = []

for row in centered:
    x = sum(row[i] * pc1[i] for i in range(cols))
    y = sum(row[i] * pc2[i] for i in range(cols))
    reduced_data.append([x, y])

# Step 7: Display results
print("===== PCA DIMENSIONALITY REDUCTION =====")

print("\nOriginal Dataset (3 Dimensions):")
for row in data:
    print(row)

print("\nReduced Dataset (2 Dimensions):")
for row in reduced_data:
    print([round(x, 3) for x in row])

print("\nOriginal Dimensions:", cols)
print("Reduced Dimensions:", 2)

print("\nPCA Completed Successfully!")
