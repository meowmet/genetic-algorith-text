import random

GENS = "abcçdefgğhıijklmnoöpqrsştuüvwxyz "
TARGET = input("enter ur target: ")
POP_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000

def random_individual():
    return ''.join(random.choice(GENS) for _ in range(len(TARGET)))

def fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET) if a == b)

def select(population):
    return max(random.sample(population, 5), key=fitness)

def crossover(parent1, parent2):
    point = random.randint(0, len(TARGET) - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual):
    return ''.join(c if random.random() > MUTATION_RATE else random.choice(GENS) for c in individual)

population = [random_individual() for _ in range(POP_SIZE)]

for generation in range(GENERATIONS):
    population = sorted(population, key=fitness, reverse=True)
    if fitness(population[0]) == len(TARGET):
        print(f"Solution found in generation {generation}: {population[0]}")
        break

    next_generation = [population[0], population[1]]  
    while len(next_generation) < POP_SIZE:
        parent1, parent2 = select(population), select(population)
        child = mutate(crossover(parent1, parent2))
        next_generation.append(child)

    population = next_generation
    if generation % 50 == 0:
        print(f"Gen {generation}: {population[0]}")

print(f"Final solution: {population[0]}")
