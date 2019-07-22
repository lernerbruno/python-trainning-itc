"""
Author: Bruno Lerner
"""

import numpy as np
from gen import Gen
from chromosome import Chromosome
from generation import Generation
import logging

GENERATION_SIZE = 50
NUMBER_OF_GENERATIONS = 50


def main():
    logging.basicConfig(filename='output.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    f = open("items.txt", 'r')
    items = np.loadtxt(f)

    gens = np.array([])
    for item in items:
        gen = Gen(item[0], item[1])
        gens = np.append(gens, gen)

    # create first chromosomes
    chromosomes = np.array([])
    for i in range(GENERATION_SIZE):
        n_of_gens = np.random.randint(1, len(gens))
        selected_gens = np.random.choice(gens, n_of_gens, replace=False)
        chromosome = Chromosome(selected_gens)
        chromosomes = np.append(chromosomes, chromosome)

    generation = Generation(chromosomes, gens)
    for i in range(NUMBER_OF_GENERATIONS):
        logging.info("Generation number {}".format(i))
        generation.selection()
        generation.crossover()
        generation.mutation()
    best = generation.get_best_chromosome()

    logging.info("Final solution:\n {}".format(best))


if __name__ == "__main__":
    main()
