"""
It makes one liners functions
Author: Bruno Lerner
"""


def ordered_digits(digits):
    '''
    it gets the index of a number in the list and repeats the word in the index by index times
    :param digits:
    :return:
    '''
    return "".join([str(x) * (ind + 1) for ind, x in enumerate(digits)])


if __name__ == "__main__":
    print(ordered_digits([2, 5, 1, 9, 2]))
