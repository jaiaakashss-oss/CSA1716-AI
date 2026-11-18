
import numpy as np

# XOR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y = np.array([[0], [1], [1], [0]])

# Neural network structure: 2-4-1
INPUTS = 2
HIDDEN = 4
OUTPUTS = 1

# Genetic Algorithm settings
POPULATION_SIZE = 30
GENERATIONS = 100
MUTATION_RATE = 0.1
ELITE_SIZE = 2

# Neural network prediction
def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def predict(chromosome, X):

    w1 = chromosome[:8].reshape(2, 4)
    b1 = chromosome[8:12]

    w2 = chromosome[12:16].reshape(4, 1)
    b2 = chromosome[16:17]

    hidden = sigmoid(np.dot(X, w1) + b1)
    output = sigmoid(np.dot(hidden, w2) + b2)

    return output

# Fitness calculation
def fitness(chromosome):

    predictions = predict(chromosome, X)

    error = np.mean((Y - predictions) ** 2)

    return 1 / (error + 0.001)

# Create initial population
population = [
    np.random.uniform(-1, 1, 17)
    for _ in range(POPULATION_SIZE)
]

# Genetic Algorithm
for generation in range(GENERATIONS):

    scores = [fitness(ind) for ind in population]

    # Sort population by fitness
    sorted_population = [
        ind for _, ind in sorted(
            zip(scores, population),
            key=lambda item: item[0],
            reverse=True
        )
    ]

    # Select best individuals
    new_population = sorted_population[:ELITE_SIZE]

    # Crossover and mutation
    while len(new_population) < POPULATION_SIZE:

        parent1 = sorted_population[np.random.randint(10)]
        parent2 = sorted_population[np.random.randint(10)]

        # Crossover
        child = np.where(
            np.random.rand(17) < 0.5,
            parent1,
            parent2
        )

        # Mutation
        for i in range(17):
            if np.random.rand() < MUTATION_RATE:
                child[i] += np.random.normal(0, 0.5)

        new_population.append(child)

    population = new_population

    best_fitness = max(scores)

    if generation % 10 == 0:
        print(
            "Generation:",
            generation,
            "Best Fitness:",
            round(best_fitness, 4)
        )

# Final best neural network
best = max(population, key=fitness)

print("\nFinal Neural Network Results")
print("--------------------------------")

predictions = predict(best, X)

for inputs, output in zip(X, predictions):
    print(
        "Input:",
        inputs,
        "Predicted Output:",
        round(float(output[0]), 3),
        "Actual Output:",
        int(Y[list(map(tuple, X)).index(tuple(inputs))][0])
    )

print("\nTraining Completed!")
