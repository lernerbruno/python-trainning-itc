"""
Author: Bruno Lerner
"""

from collections import defaultdict
import copy

def get_frequency_map():
    char_frequency = defaultdict(int)

    with open('example.txt') as f:
        f_content = f.read()

    for char in f_content:
        char_frequency[char] += 1

    return char_frequency

def filter_frequency_map(freq_map):
    copied_map = copy.deepcopy(freq_map)


def main():
    char_frenquency = get_frequency_map()




if __name__ == "__main__":
    main()
