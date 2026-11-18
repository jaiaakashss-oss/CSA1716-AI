
# Reinforcement Learning Agent using Q-Learning

import random

# Environment
states = 5
actions = 2

# Action 0 = Move Left
# Action 1 = Move Right

goal = 4

# Q-Table initialization
Q = [[0 for _ in range(actions)] for _ in range(states)]

# Learning parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 1000

# Reward function
def get_reward(state):
    if state == goal:
        return 100
    return -1

# Training the agent
for episode in range(episodes):

    state = 0

    while state != goal:

        # Choose action using epsilon-greedy policy
        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = Q[state].index(max(Q[state]))

        # Perform action
        if action == 0:
            next_state = max(0, state - 1)
        else:
            next_state = min(states - 1, state + 1)

        # Get reward
        reward = get_reward(next_state)

        # Q-Learning update
        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * max(Q[next_state]) - Q[state][action]
        )

        state = next_state

# Display Q-Table
print("===== Q-LEARNING RESULTS =====")

print("\nQ-Table:")

for i in range(states):
    print("State", i, ":", [round(x, 2) for x in Q[i]])

# Test the trained agent
print("\n===== TRAINED AGENT =====")

state = 0
path = [state]

while state != goal:
    action = Q[state].index(max(Q[state]))

    if action == 0:
        state = max(0, state - 1)
    else:
        state = min(states - 1, state + 1)

    path.append(state)

print("Agent Path:", path)
print("Goal Reached Successfully!")
