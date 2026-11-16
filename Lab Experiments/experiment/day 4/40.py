
# Backward Chaining Program

facts = {"fever", "cough"}

rules = {
    "flu": ["fever", "cough"],
    "take_rest": ["flu"],
    "recovery": ["take_rest"],
    "respiratory_problem": ["cough"]
}

def backward_chaining(goal):
    if goal in facts:
        return True

    if goal in rules:
        for condition in rules[goal]:
            if not backward_chaining(condition):
                return False
        return True

    return False


# Main Program
print("===== BACKWARD CHAINING SYSTEM =====")

goal = input("Enter the goal to prove: ").lower()

if backward_chaining(goal):
    print("\nGoal", goal, "is PROVED.")
else:
    print("\nGoal", goal, "CANNOT BE PROVED.")
