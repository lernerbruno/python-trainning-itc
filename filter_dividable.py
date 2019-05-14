"""
It makes one liners functions
Author: Bruno Lerner
"""


def filter_dividable(numbers, divisors):
    return [x for x in numbers if any([x % divisor == 0 for divisor in divisors])]


if __name__ == "__main__":
    print(filter_dividable([1, 2, 3, 4, 5, 6], [2, 3]))
