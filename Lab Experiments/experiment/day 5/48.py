
# Bayesian Network for Probabilistic Relationships

# Probability values
P_Disease = 0.01
P_NoDisease = 0.99

# Conditional probabilities
P_Fever_Disease = 0.80
P_Fever_NoDisease = 0.10

P_Cough_Disease = 0.70
P_Cough_NoDisease = 0.20

# Get user input
fever = input("Does the person have fever? (yes/no): ").lower()
cough = input("Does the person have cough? (yes/no): ").lower()

# Calculate probability of symptoms
if fever == "yes":
    p_fever_d = P_Fever_Disease
    p_fever_nd = P_Fever_NoDisease
else:
    p_fever_d = 1 - P_Fever_Disease
    p_fever_nd = 1 - P_Fever_NoDisease

if cough == "yes":
    p_cough_d = P_Cough_Disease
    p_cough_nd = P_Cough_NoDisease
else:
    p_cough_d = 1 - P_Cough_Disease
    p_cough_nd = 1 - P_Cough_NoDisease

# Bayesian probability calculation
numerator = P_Disease * p_fever_d * p_cough_d

denominator = (
    numerator +
    P_NoDisease * p_fever_nd * p_cough_nd
)

# Posterior probability
probability = numerator / denominator

# Display result
print("\n--- Bayesian Network Result ---")
print("Probability of Disease:", round(probability * 100, 2), "%")
print("Probability of No Disease:", round((1 - probability) * 100, 2), "%")

if probability > 0.5:
    print("Prediction: Disease is likely")
else:
    print("Prediction: Disease is unlikely")
