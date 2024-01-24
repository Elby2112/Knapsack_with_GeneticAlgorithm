# knapsack.py

class Knapsack:
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items

    def fitness(self, solution):
        """
        Evaluate the fitness of a solution.

        :param solution: A binary list representing the presence (1) or absence (0) of each item.
        :return: The total value of the items in the solution if it is feasible; otherwise, a low fitness value.
        """
        total_value = 0
        total_weight = 0

        for i in range(len(solution)):
            if solution[i] == 1:
                total_value += self.items[i].value
                total_weight += self.items[i].weight

        # Check if the solution violates the capacity constraint
        if total_weight > self.capacity:
            # Penalize solutions that exceed the capacity
            return 0

        return total_value
