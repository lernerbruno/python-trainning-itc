"""
Encryptor for the decrypt_2 exercise
Author: Omer Rosenbaum
"""
from random import randint

MY_SECRET = "I used something else..."

def encrypt(string):
    offset = randint(0, 24)
    encrypted = str(offset*2+4) + ","

    for character in string:
        encrypted += chr(ord(character)+offset)
    return encrypted

if __name__ == '__main__':
    print(encrypt(MY_SECRET))
