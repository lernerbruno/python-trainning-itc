"""
This file resolves the exercise zipper where you need to a list of tuples given 2 list/tuple
Author: Bruno Lerner
"""


def zipper(elem1, elem2):
    """
    This function creates a tuple with elements from both arguments and appends it to a list
    """
    list_of_tuples = []
    for i in range(min(len(elem1), len(elem2))):
        list_of_tuples.append(tuple([elem1[i], elem2[i]]))
    return list_of_tuples


if __name__ == "__main__":
    print(zipper([1,2,3], [4,5,6]))
    print(zipper([1,"hello world"], [4,5,6,7,8,9]))
