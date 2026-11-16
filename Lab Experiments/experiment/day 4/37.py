
import random

# Fitness function
def fitness(x):
    return x * x

# Generate initial population
population = [random.randint(0, 31) for _ in range(6)]

generations = 20

print("Initial Population:", population)

for generation in range(generations):

    # Selection: Choose the best individuals
    population.sort(key=fitness, reverse=True)
    parents = population[:3]

    # Crossover
    offspring = []

    while len(offspring) < 3:
        p1, p2 = random.sample(parents, 2)

        child = (p1 + p2) // 2
        offspring.append(child)

    # Mutation
    for i in range(len(offspring)):
        if random.random() < 0.2:
            offspring[i] = random.randint(0, 31)

    # New population
    population = parents + offspring

    print("Generation", generation + 1, ":", population)

# Find best solution
best = max(population, key=fitness)

print("\nBest Solution:", best)
print("Maximum Fitness Value:", fitness(best))
