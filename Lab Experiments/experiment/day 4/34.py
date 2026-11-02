
# Neural Network for Image Classification
# Pure Python - No External Libraries Required

import math
import random

random.seed(42)

# Step 1: Create a small image dataset
# 3x3 images: Vertical line = 0, Horizontal line = 1

images = [
    [0,1,0, 0,1,0, 0,1,0],
    [1,0,0, 1,0,0, 1,0,0],
    [0,0,1, 0,0,1, 0,0,1],
    [0,0,0, 1,1,1, 0,0,0],
    [1,1,1, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 1,1,1]
]

labels = [0, 0, 0, 1, 1, 1]

# Step 2: Define activation function
def sigmoid(x):
    x = max(-500, min(500, x))
    return 1 / (1 + math.exp(-x))

# Step 3: Initialize neural network
input_size = 9
hidden_size = 6
output_size = 2

weights1 = [
    [random.uniform(-1, 1) for _ in range(input_size)]
    for _ in range(hidden_size)
]

weights2 = [
    [random.uniform(-1, 1) for _ in range(hidden_size)]
    for _ in range(output_size)
]

bias1 = [0.0] * hidden_size
bias2 = [0.0] * output_size

learning_rate = 0.5

# Step 4: Forward propagation
def forward(inputs):
    hidden = []

    for i in range(hidden_size):
        total = bias1[i]

        for j in range(input_size):
            total += weights1[i][j] * inputs[j]

        hidden.append(sigmoid(total))

    outputs = []

    for i in range(output_size):
        total = bias2[i]

        for j in range(hidden_size):
            total += weights2[i][j] * hidden[j]

        outputs.append(sigmoid(total))

    return hidden, outputs

# Step 5: Train the neural network
print("Training Neural Network...")

for epoch in range(3000):

    for inputs, label in zip(images, labels):

        target = [0, 0]
        target[label] = 1

        hidden, outputs = forward(inputs)

        # Calculate output errors
        output_errors = [
            outputs[i] - target[i]
            for i in range(output_size)
        ]

        # Calculate hidden layer errors
        hidden_errors = []

        for j in range(hidden_size):
            error = 0

            for i in range(output_size):
                error += output_errors[i] * weights2[i][j]

            error *= hidden[j] * (1 - hidden[j])
            hidden_errors.append(error)

        # Update output weights
        for i in range(output_size):
            for j in range(hidden_size):
                weights2[i][j] -= (
                    learning_rate * output_errors[i] * hidden[j]
                )

            bias2[i] -= learning_rate * output_errors[i]

        # Update input weights
        for i in range(hidden_size):
            for j in range(input_size):
                weights1[i][j] -= (
                    learning_rate * hidden_errors[i] * inputs[j]
                )

            bias1[i] -= learning_rate * hidden_errors[i]

print("Training Completed Successfully!")

# Step 6: Test image classification
test_images = [
    [0,1,0, 0,1,0, 0,1,0],
    [0,0,0, 1,1,1, 0,0,0]
]

class_names = ["Vertical Line", "Horizontal Line"]

print("\nIMAGE CLASSIFICATION RESULTS")
print("-----------------------------")

for index, image in enumerate(test_images):

    hidden, prediction = forward(image)

    predicted_class = prediction.index(max(prediction))

    print("\nTest Image:", index + 1)

    print("Image:")
    for i in range(0, 9, 3):
        print(image[i:i+3])

    print("Predicted Class:", class_names[predicted_class])
    print("Confidence:", round(max(prediction) * 100, 2), "%")

print("\nNeural Network Image Classification")
print("Program Executed Successfully!")
