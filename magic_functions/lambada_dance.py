"""
Author: Bruno Lerner
"""

from functools import reduce


def main():
    # divides number and module
    div_and_mod = lambda a, b: (int(a / b), a % b) if b != 0 else "The divisor can't be zero"
    # print number if its positive and 0 if its negative
    non_negative = lambda a: 0 if a < 0 else a
    # it duplicates each digit by 2
    double_digits = lambda x: int(reduce(lambda c, d: c + d * 2, str(x), ""))

    print(div_and_mod(2, 0))
    print(div_and_mod(2, 3))
    print(non_negative(-3))
    print(non_negative(3))
    print(double_digits(23578))


if __name__ == "__main__":
    main()
