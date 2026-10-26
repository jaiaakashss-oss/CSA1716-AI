
# Diet Suggestion System Based on Disease

def diet_suggestion(disease):
    if disease == "diabetes":
        print("Suggested diet: Whole grains, vegetables, pulses, and low-sugar fruits.")

    elif disease == "hypertension":
        print("Suggested diet: Fruits, vegetables, and low-sodium foods.")

    elif disease == "anemia":
        print("Suggested diet: Iron-rich foods such as spinach, beans, and lentils.")

    elif disease == "obesity":
        print("Suggested diet: Vegetables, fruits, whole grains, and balanced portions.")

    elif disease == "heart disease":
        print("Suggested diet: Vegetables, whole grains, and foods low in saturated fat.")

    else:
        print("No diet suggestion available for this condition.")

# Main program
print("Diet Suggestion System")
print("Available conditions: diabetes, hypertension, anemia, obesity, heart disease")

disease = input("Enter the disease: ").lower()

diet_suggestion(disease)
