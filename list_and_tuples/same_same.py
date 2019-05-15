"""
This code makes a function that sums elements in a tuple no matter its type

Author: Bruno Lerner
"""


def samesame(summing_things):
    """
    This function checks if the type of every element in the list, and if they are all the same the function gives its sum
    """
    sum_result = summing_things[0]
    for i in range(len(summing_things)):
        if i != 0:
            sum_result += summing_things[i]
    return sum_result


if __name__ == "__main__":
    print(samesame([2, 4, 5]))
    print(samesame(['a', 'b', 'c']))
    print(samesame([[1, 2], [3, 4]]))
