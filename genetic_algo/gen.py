class Gen:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return "Gen(Value={}, Weight={})".format(self.value, self.weight)

    def __eq__(self, other):
        if self.value == other.value and self.weight == other.weight:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

