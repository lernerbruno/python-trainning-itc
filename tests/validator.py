"""
This is a file for an exercise, which the objective is to multiply a chain of numbers
Author: Bruno Lerner
"""


def multiplier(numbers):
    """
    it gets a list of numbers and multiply them
    :param numbers:
    :return: multiplied numbers
    """
    result = 1
    for number in numbers:
        result *= number
    return result

def isvalid(numbers):
    """
    it checks if all info provided are numbers

    """
    numbers = str(numbers).split(" ")
    return all(x.lstrip("-").isnumeric() for x in numbers)

def main():
    numbers_to_multiply = input("Please enter sequence of numbers that will be multiplied")
    while not isvalid(numbers_to_multiply):
        numbers_to_multiply = input("This is not valid. Please enter sequence of numbers that will be multiplied")
    numbers = str(numbers_to_multiply).split(" ")
    numbers = [int(x) for x in numbers]

    calculation_result = multiplier(numbers)

    print(calculation_result)

def assert_multiplier():
    assert multiplier([0, 2, 3, 4]) == 0
    assert multiplier([3, 3]) == 9
    assert multiplier([12, 4, 5]) == 240
    assert multiplier([5]) == 5

def assert_validator():
    assert not isvalid('[1] 2')
    assert not isvalid('a 2')
    assert isvalid('2 2')
    assert isvalid('2 -2')


if __name__ == '__main__':
    main()

    assert_multiplier()
    assert_validator()