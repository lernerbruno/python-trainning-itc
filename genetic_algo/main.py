"""
Author: Bruno Lerner
"""

import numpy as np
from gen import Gen
from chromosome import Chromosome
MAX_WEIGHT = 15

def main():
    f = open("items.txt", 'r')
    items = np.loadtxt(f)

    gens = []
    for item in items:
        gen = Gen(item[0], item[1])
        gens.append(gen)

    # create first chromosome
    total_weight = 0
    selected_gens = []
    while total_weight <= MAX_WEIGHT:
        selected = np.random.choice(gens, 1, replace=False)
        if total_weight + selected.weight <= MAX_WEIGHT:

    chromosome = Chromosome(selected_gens)





if __name__ == "__main__":
    main()
