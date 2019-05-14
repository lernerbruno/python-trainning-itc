#!/usr/bin/python -tt
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##   instructions were changed to deal with proper handling of punctuation
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in alphabetical order. Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. Remember to deal with punctuation. For example:
Alice     Alice:     "Alice      Alice,    Alice"   are all the same word   >>>> alice

BUT - In words like  Alice's   or   they're, the apostrophe is part of the word
so don't split them into into    Alice + s    or   they  +  re

3. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

4. Please use functions to prevent writing duplicate code.

In addition to  print_words(filename) and print_top(filename) functions,
you must write additional functions that read a file, build a word/count dict
and so on.


"""

import sys, os

# constants used for main()
REQUIRED_NUM_OF_ARGS = 3
ARG_OPTION = 1
ARG_FILE_NAME = 2
BLACKLIST_CHARS = ',":\n.!)(*-`;\'_[]{}?'
WORDS_LIMIT = 20

def clean_word(word):
    """
    it removes some characters and lower case it
    :param word:
    :return:
    """
    return word.lower().strip(BLACKLIST_CHARS)


def read_file(filename):
    """
    it reads the file and returns a list with each word, split by space
    :param filename:
    :return:
    """
    try:
        f = open(filename, 'r')
        f_content = f.read()
        f.close()
        return f_content.split()
    except FileNotFoundError:
        print('The file does not exist')
        return ''


def get_dict_of_words(file_words):
    """
    it create a dict and count each appearance of each word
    :param file_words:
    :return:
    """
    words_counter = {}
    for word in file_words:
        if word != "":
            cleaned_word = clean_word(word)
            if words_counter.get(cleaned_word) is None:
                words_counter[cleaned_word] = 1
            else:
                words_counter[cleaned_word] += 1
    return words_counter


def print_words(filename):
    """
    It prints the dict of appearance of each word in the file in alphabetical order
    :param filename:
    :return:
    """
    file_words = read_file(filename)
    words_counter = get_dict_of_words(file_words)
    for word, number_of_appearance in sorted(words_counter.items()):
        print(word, number_of_appearance)


def print_top(filename):
    """
    It prints the dict of appearance of each word in the file in word count order
    :param filename:
    :return:
    """
    file_words = read_file(filename)
    words_counter = get_dict_of_words(file_words)
    i = 0
    for w in sorted(words_counter, key=words_counter.get, reverse=True):
        if i < WORDS_LIMIT:
            print(w, words_counter[w])
        i += 1


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    """
    get user input - file name and which option --cout or --topcount
    read text file, count and sort words
    """

    if len(sys.argv) != REQUIRED_NUM_OF_ARGS:
        print("usage: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[ARG_OPTION]
    filename = sys.argv[ARG_FILE_NAME]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == "__main__":
    main()
