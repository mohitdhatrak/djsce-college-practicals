import random


# returns a list of target length (here 8), with random 0s and 1s
def generate_individual(length):
    arr = []
    for _ in range(length):
        arr.append(random.choice([0, 1]))
    return arr


# returns count of matching bits in individual and target
def calculate_fitness(individual, target):
    count = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            count += 1
    return count


# returns a child made from parents by randomly picking a split point
# split both parents at that point, take either half from each parent to make child
def crossover(parent1, parent2):
    split_point = random.randint(0, len(parent1) - 1)
    child = parent1[:split_point] + parent2[split_point:]
    return child


# returns mutated child as per the mutation rate
# learn - bitwise XOR between bit and result of expression -> (random.random() < mutation_rate))
# this expression evaluates to True with a probability of mutation_rate
def mutate(individual, mutation_rate):
    child = []
    for bit in individual:
        child.append(bit ^ (random.random() < mutation_rate))
    return child


def genetic_algorithm(target, population_size, mutation_rate, generations):
    individual_length = len(target)  # len -> 8

    # step 1 - generate population, as per target length (here 8) and population size
    population = []
    for _ in range(population_size):
        individual = generate_individual(individual_length)
        population.append(individual)

    # step 2 - for each generation,
    # calculate fitness for whole population and sort the population in descending order of fitness
    # highest fitness value means the best individual, now compare it with target
    # if target is exact same then target reached -> stop the loop
    for generation in range(generations):
        population = sorted(
            population,
            key=lambda individual: calculate_fitness(individual, target),
            reverse=True,
        )
        best_individual = population[0]

        if calculate_fitness(best_individual, target) == individual_length:
            print(f"Target reached in generation {generation + 1}!")
            break

        # step 3 - target not reached, so generate new population before again checking fitness
        # this is called evolution of the population -> has 3 stages

        # stage 1 - SELECTION -> add best individual to new population
        # fill remaining population by stage 2 and 3
        new_population = [best_individual]

        while len(new_population) < population_size:  # till we fill whole population
            # stage 2 - CROSSOVER -> means mating, so we need 2 random individuals from population as parents
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)

            # stage 3 - MUTATION -> from above generated child, we mutate it to get the final new individual
            child = mutate(child, mutation_rate)

            # finally append the child to new population
            new_population.append(child)

        # set population array, again go to step 2
        population = new_population

    return population[0]


target_binary = [1, 0, 1, 1, 0, 1, 0, 1]  # len -> 8
population_size = 100
mutation_rate = 0.01
generations = 1000

result = genetic_algorithm(target_binary, population_size, mutation_rate, generations)

print(f"Best individual of the evolved population: {result}")
