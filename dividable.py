"""
It makes one liners functions
Author: Bruno Lerner
"""


def dividable(numbers, divisor):
    return all([x % divisor == 0 for x in numbers])


if __name__ == "__main__":
    print(dividable([3, 6, 9, 12], 3))
    print(dividable([3, 6, 9, 13], 3))
