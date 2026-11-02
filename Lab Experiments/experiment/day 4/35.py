# Decision Tree for a Simple Classification Problem
# No external libraries required

# Training dataset
# (Weather, Wind) -> Play

training_data = [
    ("Sunny", "Weak", "Yes"),
    ("Sunny", "Strong", "No"),
    ("Rainy", "Weak", "Yes"),
    ("Rainy", "Strong", "No"),
    ("Overcast", "Weak", "Yes"),
    ("Overcast", "Strong", "Yes")
]

# Decision Tree Function
def decision_tree(weather, wind):

    if weather == "Overcast":
        return "Yes"

    elif weather == "Sunny":
        if wind == "Weak":
            return "Yes"
        else:
            return "No"

    elif weather == "Rainy":
        if wind == "Weak":
            return "Yes"
        else:
            return "No"

    else:
        return "Invalid Input"

# Display Training Data
print("DECISION TREE CLASSIFICATION")
print("----------------------------")

print("\nTraining Data:")
for data in training_data:
    print(data)

# Test Prediction
print("\nEnter Test Data")
weather = input("Weather (Sunny/Rainy/Overcast): ")
wind = input("Wind (Weak/Strong): ")

result = decision_tree(weather, wind)

print("\nPrediction:", result)

print("\nDecision Tree Classification Completed Successfully!")
