class Chromosome:

    def __init__(self, gens):
        self.set_of_gens = gens
        self.score = 0

    def fitness(self):
        total_value = 0
        for gen in self.set_of_gens:
            total_value += gen.value

        self.score = total_value
        return total_value
