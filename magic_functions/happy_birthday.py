"""
It generates a happy birthday song without any for and while loops, only using magic functions
Author: Bruno Lerner
"""

import functools

HAPPY = "Happy Birthday "
DEAR = "dear %s"
TO_YOU = "to you"


def generate_song(a, b, name):
    """
    It mounts the verse in the song accordingly to the number on range(4)
    :param a: current string
    :param b: next element on iterator
    :param name: custom param
    :return:
    """
    end_char = '\n' if b != 3 else ''
    end_sentence = DEAR % name if b % 4 == 2 else TO_YOU
    return a + HAPPY + end_sentence + end_char


def happy_birthday(name):
    """
    It reduces the range(4) iterator to generate 4 verses of the song
    :param name:
    :return:
    """
    song = functools.reduce(functools.partial(generate_song, name=name), range(4), "")
    return song


def main():
    print(happy_birthday('Dani'))


if __name__ == "__main__":
    main()
