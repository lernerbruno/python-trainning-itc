class Population:
    def __init__(self, chromosomes):
        self.set_of_chromosomes = chromosomes

    def selection(self):
        sorted_chromosomes = sorted(self.set_of_chromosomes, key=lambda a: a.score)


