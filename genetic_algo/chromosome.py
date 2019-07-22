import numpy as np
from gen import Gen


class Chromosome:
    MAX_WEIGHT = 15

    def __init__(self, gens):
        self.set_of_gens = np.unique(gens)
        self.score, self.total_weight = self.fitness()

    def fitness(self):
        total_value = 0
        total_weight = 0

        for gen in self.set_of_gens:
            total_value += gen.value
            total_weight += gen.weight

        if total_weight > self.MAX_WEIGHT:
            return 0, total_weight

        return total_value, total_weight

    def __repr__(self):
        return "Your solution bag is {}\n Total value: {}\n Total weight: {}".format(
            list(self.set_of_gens).__repr__(), self.score, self.total_weight)

    def __len__(self):
        return len(self.set_of_gens)


# Tests
gens = np.array([Gen(3, 8), Gen(8, 2), Gen(5, 2), Gen(10, 2)])
test_chromo = Chromosome(gens)
assert test_chromo.score == 26
assert test_chromo.total_weight == 14
