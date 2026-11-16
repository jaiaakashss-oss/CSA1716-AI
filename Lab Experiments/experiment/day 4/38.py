
def medical_diagnosis():
    print("===== MEDICAL DIAGNOSIS SYSTEM =====")
    print("Answer the following questions with yes or no.\n")

    fever = input("Do you have fever? ").lower()
    cough = input("Do you have cough? ").lower()
    cold = input("Do you have a cold? ").lower()
    headache = input("Do you have headache? ").lower()
    sneezing = input("Do you have sneezing? ").lower()
    body_pain = input("Do you have body pain? ").lower()

    print("\n===== DIAGNOSIS RESULT =====")

    if fever == "yes" and cough == "yes" and body_pain == "yes":
        print("Possible Diagnosis: Flu")

    elif cold == "yes" and sneezing == "yes":
        print("Possible Diagnosis: Common Cold")

    elif fever == "yes" and headache == "yes":
        print("Possible Diagnosis: Possible Fever-related illness")

    elif cough == "yes":
        print("Possible Diagnosis: Possible Respiratory Infection")

    else:
        print("Diagnosis: No matching condition found.")

    print("\nPlease consult a qualified doctor for proper diagnosis.")


medical_diagnosis()
