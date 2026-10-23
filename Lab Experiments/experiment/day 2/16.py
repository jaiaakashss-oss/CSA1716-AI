

# Input data (AND gate)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Expected output
y = [0, 0, 0, 1]

# Create the feed-forward neural network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='relu',
    solver='lbfgs',
    max_iter=2000,
    random_state=1
)

# Train the network
model.fit(X, y)

# Test the network
print("Feed Forward Neural Network")
for inputs in X:
    prediction = model.predict([inputs])
    print(inputs, "->", prediction[0])
