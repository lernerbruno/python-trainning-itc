#!/usr/bin/python -tt
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.
"""

import random
import sys
import os

NUMBER_OF_ARGS = 2
FILE_NAME = 1
BLACKLIST_CHARS = ',":\n.!)(*-`;\'_[]{}?'
NUMBER_OF_WORDS = 200


def clean_word(word):
    """
    it removes some characters and lower case it
    :param word:
    :return:
    """
    return word.strip(BLACKLIST_CHARS)


def read_file(filename):
    """
    it reads the file and returns a list with each word, split by space
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    f_content = f.read()
    f.close()
    return f_content.split()


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    words = read_file(filename)
    mimic = {"": [clean_word(words[0])]}

    for i in range(len(words)):
        curr_word = words[i]
        next_word = words[i + 1] if i < len(words) - 1 else ""
        cleaned_word = clean_word(curr_word)
        cleaned_next_word = clean_word(next_word)

        if cleaned_word != "":
            if mimic.get(cleaned_word) is None:
                mimic[cleaned_word] = [cleaned_next_word]
            else:
                curr_list = mimic.get(cleaned_word)
                curr_list.append(cleaned_next_word)
                mimic[cleaned_word] = curr_list
    return mimic


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    random_text = ""
    i = 0
    while i < NUMBER_OF_WORDS:
        possible_words = mimic_dict.get(word) if mimic_dict.get(word) is not None else mimic_dict.get("")[0]
        # print(possible_words)
        chosen_word = random.choice(possible_words)
        random_text += random.choice(possible_words) + ' '
        word = chosen_word
        i += 1
    print(random_text)
    return


def main():
    """ Provided main(), calls mimic_dict() and mimic() """
    try:
        if len(sys.argv) != NUMBER_OF_ARGS:
            print("usage: ./mimic.py file-to-read")
            sys.exit(1)

        my_dict = mimic_dict(sys.argv[FILE_NAME])
        print_mimic(my_dict, "")
    except FileNotFoundError:
        print("File not found, please provide an existing file")


if __name__ == "__main__":
    main()
