"""
This is an example file that shows usage of assert in order to test a function.
Authors: Omer Rosenbaum, Shay Sadovsky.
"""

def factorial(number):
    """Returns the factorial result of a number.
    number - is assumed to be a non-negative number of type int.
    In case of an error, returns -1"""
    if number < 0:
        raise ValueError("Factorial is undefined for negative values!")
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

if __name__ == "__main__":
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720