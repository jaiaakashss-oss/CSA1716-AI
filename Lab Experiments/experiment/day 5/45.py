
# Markov Chain Model for Predicting Sequences

import random

# Training sequence
sequence = [
    'A', 'B', 'A', 'C', 'A',
    'B', 'A', 'C', 'A', 'B',
    'A', 'C'
]

# Step 1: Build transition model
markov_chain = {}

for i in range(len(sequence) - 1):

    current_state = sequence[i]
    next_state = sequence[i + 1]

    if current_state not in markov_chain:
        markov_chain[current_state] = {}

    if next_state not in markov_chain[current_state]:
        markov_chain[current_state][next_state] = 0

    markov_chain[current_state][next_state] += 1

# Step 2: Convert counts into probabilities
for state in markov_chain:

    total = sum(markov_chain[state].values())

    for next_state in markov_chain[state]:
        markov_chain[state][next_state] /= total

# Step 3: Predict next state
def predict_next(current_state):

    if current_state not in markov_chain:
        return None

    transitions = markov_chain[current_state]

    next_state = max(
        transitions,
        key=transitions.get
    )

    return next_state

# Step 4: Display transition probabilities
print("===== MARKOV CHAIN MODEL =====")

print("\nTransition Probabilities:")

for state, transitions in markov_chain.items():
    print(state, "->", transitions)

# Step 5: Predict sequence
current = 'A'

print("\nStarting State:", current)
print("Predicted Sequence:")

for i in range(5):

    next_state = predict_next(current)

    if next_state is None:
        print("No prediction available")
        break

    print(current, "->", next_state)

    current = next_state

print("\nSequence Prediction Completed!")
