"""
Author: Bruno Lerner
"""
import re

NEWLINE_CHAR = "\\n"
UNIQUE_CHAR = "&"

def decipher(message):
    cipher = {'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y', 'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q',
              'F': 'k', 'O': 'N', 'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l',
              'g': 'S', 'f': 'x', 'x': 'c', 'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P', 'o': 'Q', 'i': 'I', 'M': 'd',
              't': 'U', 'H': 'V', 'X': 'i', 'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z',
              'G': 'F', 'A': 'W', 'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z', 'q': 'p', 'D': 'v', 'I': 'g', 'n': 'h',
              'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J', 'Q': 'E', 'e': 'Y', 'r': 'R',
              'E': 'm'}
    deciphered_message = ""

    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            char_to_replace = (list(cipher.keys())[list(cipher.values()).index(char)])
        else:
            char_to_replace = char
        deciphered_message += char_to_replace
    return deciphered_message


def reverse_words(message):
    reversed_words = re.compile("\d").split(message)
    return " ".join([x[::-1] for x in reversed_words])


def main():
    f = open('encrypted_string.txt', 'r')
    encoded_message = f.read()
    f.close()
    encoded_message = encoded_message.replace(NEWLINE_CHAR, UNIQUE_CHAR)
    deciphered = decipher(encoded_message)
    decoded_message = reverse_words(deciphered)

    decoded_message = decoded_message.replace(UNIQUE_CHAR, '\n')
    print(decoded_message)


if __name__ == "__main__":
    main()
