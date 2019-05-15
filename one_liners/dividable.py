"""
It makes one liners functions
Author: Bruno Lerner
"""


def dividable(numbers, divisor):
    '''
    it generates a list with bool values for each word, checking if its divisible by some number and checks if everything is true
    :param numbers:
    :param divisor:
    :return:
    '''
    return all([x % divisor == 0 for x in numbers])


if __name__ == "__main__":
    print(dividable([3, 6, 9, 12], 3))
    print(dividable([3, 6, 9, 13], 3))
