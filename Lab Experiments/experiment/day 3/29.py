
# Forward Chaining using Python

# Initial Facts
facts = {"A", "B"}

# Rules (IF conditions THEN conclusion)
rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D", "E"}, "F"),
    ({"C", "D"}, "G")
]

def forward_chaining(facts, rules):
    print("Initial Facts:", facts)

    while True:
        new_fact_added = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print("New Fact Derived:", conclusion)
                new_fact_added = True

        if not new_fact_added:
            break

    print("\nFinal Facts:", facts)


# Main Program
forward_chaining(facts, rules)
