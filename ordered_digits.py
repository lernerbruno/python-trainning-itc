"""
It makes one liners functions
Author: Bruno Lerner
"""


def ordered_digits(digits):
    return "".join([str(x) * (ind + 1) for ind, x in enumerate(digits)])


if __name__ == "__main__":
    print(ordered_digits([2, 5, 1, 9, 2]))
