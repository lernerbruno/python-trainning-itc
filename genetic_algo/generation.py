import numpy as np
from chromosome import Chromosome
import logging
from gen import Gen

CROSSOVER_SPLIT = 2
N_OF_PARENTS = 2
N_OF_MUTATIONS = 2
N_OF_SELECTION_REMOVES = 4


class Generation:
    logging.basicConfig(filename='output.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def __init__(self, chromosomes, gens):
        self.set_of_chromosomes = chromosomes
        self.available_gens = gens

    def selection(self):
        logging.info("Selection of best chromosomes...")
        self.set_of_chromosomes = sorted(self.set_of_chromosomes, key=lambda a: a.score, reverse=True)[
                                  :-N_OF_SELECTION_REMOVES]
        best_chromosome = self.set_of_chromosomes[0]
        logging.info("Best Chromosome of the generation: \n{}".format(best_chromosome))

    def crossover(self):
        logging.info("Crossover on current generation...")

        parent_chromosomes = np.random.choice(self.set_of_chromosomes, N_OF_PARENTS, replace=False)

        while any(map(lambda parent: len(parent.set_of_gens) <= CROSSOVER_SPLIT, parent_chromosomes)):
            parent_chromosomes = np.random.choice(self.set_of_chromosomes, N_OF_PARENTS)

        for i in range(N_OF_PARENTS):
            child_gens = np.concatenate((parent_chromosomes[i].set_of_gens[:-CROSSOVER_SPLIT],
                                         parent_chromosomes[(i + 1) % CROSSOVER_SPLIT].set_of_gens[-CROSSOVER_SPLIT:]))
            child_chromo = Chromosome(np.unique(child_gens))
            self.set_of_chromosomes = np.append(self.set_of_chromosomes, child_chromo)

        self.set_of_chromosomes = sorted(self.set_of_chromosomes, key=lambda a: a.score, reverse=True)

    def mutation(self):
        logging.info("Mutating current generation...")
        chromosomes_to_mutate = np.random.choice(self.set_of_chromosomes, N_OF_MUTATIONS)

        for c in chromosomes_to_mutate:
            gen_to_replace = np.random.choice(self.available_gens)
            index_to_replace = np.random.randint(0, len(c))
            set_of_gens = c.set_of_gens.copy()
            set_of_gens[index_to_replace] = gen_to_replace
            new_chromo = Chromosome(np.unique(set_of_gens))
            self.set_of_chromosomes = np.append(self.set_of_chromosomes, new_chromo)

        self.set_of_chromosomes = sorted(self.set_of_chromosomes, key=lambda a: a.score, reverse=True)

    def get_best_chromosome(self):
        return sorted(self.set_of_chromosomes, key=lambda a: a.score, reverse=True)[0]


# Tests
gens = np.array([Gen(3, 8), Gen(8, 2), Gen(5, 2), Gen(10, 2)])
gens_2 = np.array([Gen(3, 8), Gen(8, 12), Gen(5, 2), Gen(10, 2)])
gens_3 = np.array([Gen(10, 8), Gen(8, 2), Gen(5, 2), Gen(10, 2)])
gens_4 = np.array([Gen(7, 5), Gen(8, 2), Gen(5, 2), Gen(10, 2)])
gens_5 = np.array([Gen(15, 8), Gen(8, 2), Gen(5, 2), Gen(10, 2)])
gens_6 = np.array([Gen(10, 3), Gen(8, 5), Gen(5, 2), Gen(3, 4)])
test_chromo = Chromosome(gens)
test_chromo_2 = Chromosome(gens_2)
test_chromo_3 = Chromosome(gens_3)
test_chromo_4 = Chromosome(gens_4)
test_chromo_5 = Chromosome(gens_5)
test_chromo_6 = Chromosome(gens_6)

f = open("items.txt", 'r')
items = np.loadtxt(f)

available_gens = np.array([])
for item in items:
    gen = Gen(item[0], item[1])
    available_gens = np.append(available_gens, gen)

generation = Generation(np.array([test_chromo, test_chromo_2, test_chromo_3, test_chromo_4, \
                                  test_chromo_5, test_chromo_6]), available_gens)

old_size = len(generation.set_of_chromosomes)
generation.selection()
new_size = len(generation.set_of_chromosomes)
assert old_size == new_size + N_OF_SELECTION_REMOVES

generation.crossover()
new_size = len(generation.set_of_chromosomes)
assert old_size + N_OF_PARENTS == new_size + N_OF_SELECTION_REMOVES

generation.crossover()
new_size = len(generation.set_of_chromosomes)
assert old_size + N_OF_PARENTS + N_OF_MUTATIONS == new_size + N_OF_SELECTION_REMOVES
