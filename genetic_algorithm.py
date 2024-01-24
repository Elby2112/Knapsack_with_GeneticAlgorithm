# genetic_algorithm.py

import random

class GeneticAlgorithm:
    def __init__(self, knapsack, population_size, generations, crossover_rate, mutation_rate):
        self.knapsack = knapsack
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

        # Initialize population
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            solution = [random.choice([0, 1]) for _ in range(len(self.knapsack.items))]
            population.append(solution)
        return population

    def selection(self):
        tournament_size = 2
        selected_parents = []

        for _ in range(self.population_size):
            tournament = random.sample(self.population, tournament_size)
            selected_parents.append(max(tournament, key=lambda x: self.knapsack.fitness(x)))

        return selected_parents

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        else:
            return parent1, parent2

    def mutation(self, individual):
        mutated_individual = individual.copy()
        for i in range(len(mutated_individual)):
            if random.random() < self.mutation_rate:
                mutated_individual[i] = 1 - mutated_individual[i]
        return mutated_individual

    def evolve(self):
        best_solution = None
        best_fitness = float('-inf')

        for generation in range(self.generations):
            # Selection
            parents = self.selection()

            # Crossover
            new_population = []
            for i in range(0, self.population_size, 2):
                parent1, parent2 = parents[i], parents[i + 1]
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([child1, child2])

            # Mutation
            new_population = [self.mutation(individual) for individual in new_population]

            # Elitism: Keep the best solution from the previous generation
            best_previous = max(self.population, key=lambda x: self.knapsack.fitness(x))
            new_population[0] = best_previous

            # Update population
            self.population = new_population

            # Find and store the best solution in each generation
            current_best_solution = max(self.population, key=lambda x: self.knapsack.fitness(x))
            current_best_fitness = self.knapsack.fitness(current_best_solution)

            if current_best_fitness > best_fitness:
                best_solution = current_best_solution
                best_fitness = current_best_fitness

            # Display the best solution in each generation
            print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

        # Final result
        print("\nFinal Result:")
        print(f"Best Solution: {best_solution}")
        print(f"Best Fitness: {best_fitness}")
        print("\nSelected Items:")
        for i, included in enumerate(best_solution):
            if included:
                print(f"- {self.knapsack.items[i].name}")
