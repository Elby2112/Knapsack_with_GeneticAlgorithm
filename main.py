#main.py

from item import Item
from knapsack import Knapsack
from genetic_algorithm import GeneticAlgorithm
# Sample items
laptop = Item("Laptop", 800, 3)
tablet = Item("Tablet", 400, 1)
headphones = Item("Headphones", 150, 1)
notebook = Item("Notebook", 100, 1)
mouse = Item("Mouse", 50, 0.5)
water_bottle = Item("Water Bottle", 30, 0.5)
snack_bar = Item("Snack Bar", 20, 0.2)
sunglasses = Item("Sunglasses", 70, 0.1)
umbrella = Item("Umbrella", 40, 0.7)
book = Item("Book", 120, 1)

# Initialize the knapsack problem
knapsack_capacity = 5
items = [laptop, tablet, headphones, notebook, mouse, water_bottle, snack_bar, sunglasses, umbrella, book]
knapsack = Knapsack(knapsack_capacity, items)

# Initialize the genetic algorithm
population_size = 10
generations = 20
crossover_rate = 0.7
mutation_rate = 0.1

genetic_algorithm = GeneticAlgorithm(knapsack, population_size, generations, crossover_rate, mutation_rate)

# Run the genetic algorithm
genetic_algorithm.evolve()