"""
Encryptor for the decrypt_1 exercise
Author: Omer Rosenbaum
"""
from random import randint

MY_SECRET = "I used something else..."

def encrypt(string):
    encrypted = ""
    for character in string:
        offset = randint(0, 9)
        encrypted += str(offset)
        encrypted += chr(ord(character)+offset)
    return encrypted

if __name__ == '__main__':
    print(encrypt(MY_SECRET))
