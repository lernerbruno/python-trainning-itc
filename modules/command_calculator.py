"""
It creates a command line tool for calculating numbers
Author: Bruno Lerner
"""
import argparse


def add(first, second):
    """
    it sums 2 numbers
    """
    return first + second


def subtract(first, second):
    """
    it subtracts 2 numbers
    """
    return first - second


def multiply(first, second):
    """
    it multiplicates 2 numbers
    """
    return first * second


def divide(first, second):
    """
    it divides 2 numbers
    """
    if second == 0:
        return 'Invalid operation'
    return first / second


def define_arguments():
    """
    Define the command line options and commands
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], type=str)
    parser.add_argument("first_number", help="The first number that will be calculated", type=float)
    parser.add_argument("second_number", help="The second number that will be calculated", type=float)
    parser.add_argument("-w", help="Add this option if you want a good morning message", action="store_true")

    return parser.parse_args()


def main():
    args = define_arguments()

    # locals() does exactly that for you
    functions_mapping = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if args.w:
        print("Good Morning :)")

    print(functions_mapping[args.operation](args.first_number, args.second_number))


def assert_sum():
    assert add(1.0, -2.0) == -1.0
    assert add(2, 4) == 6
    assert add(-5, 0) == -5
    assert add(-5.2, 0.2) == -5.0


def assert_subtract():
    assert subtract(1, 1) == 0
    assert subtract(1.0, 2.0) == -1.0
    assert subtract(-5, -2) == -3


def assert_multiply():
    assert multiply(1, 1) == 1
    assert multiply(1.0, 0.0) == 0.0
    assert multiply(-5, -2) == 10


def assert_divide():
    assert divide(1, 0) == 'Invalid operation'
    assert divide(1.0, 2.0) == 0.5
    assert divide(-6, -2) == 3


if __name__ == "__main__":
    main()
