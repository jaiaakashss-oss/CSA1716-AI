
# Medical Diagnosis using Prolog Concepts

def medical_diagnosis():
    print("===== MEDICAL DIAGNOSIS SYSTEM =====")

    fever = input("Do you have fever? (yes/no): ").lower()
    cough = input("Do you have cough? (yes/no): ").lower()
    headache = input("Do you have headache? (yes/no): ").lower()
    cold = input("Do you have cold? (yes/no): ").lower()
    body_pain = input("Do you have body pain? (yes/no): ").lower()

    # Diagnosis rules
    if fever == "yes" and cough == "yes" and cold == "yes":
        print("\nPossible Diagnosis: Flu")

    elif fever == "yes" and headache == "yes" and body_pain == "yes":
        print("\nPossible Diagnosis: Viral Fever")

    elif cold == "yes" and cough == "yes" and fever == "no":
        print("\nPossible Diagnosis: Common Cold")

    elif headache == "yes" and fever == "no":
        print("\nPossible Diagnosis: Headache")

    else:
        print("\nDiagnosis not identified.")
        print("Please consult a doctor.")

    print("\nThank you!")


medical_diagnosis()
