
# Backward Chaining using Python

# Knowledge Base (Facts)
facts = {"A", "B"}

# Rules (Conditions -> Conclusion)
rules = {
    "C": ["A", "B"],
    "D": ["C"],
    "E": ["C", "D"],
    "F": ["E"]
}

# Backward Chaining Function
def backward_chaining(goal):
    print("Checking goal:", goal)

    # Check whether goal is a known fact
    if goal in facts:
        print(goal, "is a fact.")
        return True

    # Check rules for the goal
    if goal in rules:
        for condition in rules[goal]:
            if not backward_chaining(condition):
                return False

        print(goal, "is proved.")
        return True

    print(goal, "cannot be proved.")
    return False


# Main Program
goal = input("Enter the goal: ").upper()

if backward_chaining(goal):
    print("\nGoal is TRUE")
else:
    print("\nGoal is FALSE")
