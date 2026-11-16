
# Forward Chaining Program

facts = {"fever", "cough"}

rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "take_rest"),
    ({"take_rest"}, "recovery"),
    ({"cough"}, "respiratory_problem"),
    ({"fever"}, "high_temperature")
]

def forward_chaining(facts, rules):
    print("Initial Facts:", facts)

    new_fact_found = True

    while new_fact_found:
        new_fact_found = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("New Fact Derived:", conclusion)
                    new_fact_found = True

    return facts


result = forward_chaining(facts, rules)

print("\nFinal Knowledge Base:")
for fact in sorted(result):
    print(fact)
