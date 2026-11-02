
# Linear Regression using Pure Python

# Dataset
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

n = len(x)

# Calculate mean
mean_x = sum(x) / n
mean_y = sum(y) / n

# Calculate slope
numerator = 0
denominator = 0

for i in range(n):
    numerator += (x[i] - mean_x) * (y[i] - mean_y)
    denominator += (x[i] - mean_x) ** 2

slope = numerator / denominator

# Calculate intercept
intercept = mean_y - slope * mean_x

# Display results
print("LINEAR REGRESSION")
print("-----------------------")

print("Slope:", slope)
print("Intercept:", intercept)

# Predict values
print("\nPredicted Values:")

for i in range(n):
    prediction = slope * x[i] + intercept
    print("X =", x[i], " Y =", prediction)

# Predict a new value
new_x = 6
new_y = slope * new_x + intercept

print("\nPrediction for X =", new_x)
print("Predicted Y =", new_y)

print("\nLinear Regression Completed Successfully!")
