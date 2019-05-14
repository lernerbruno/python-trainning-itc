"""
It makes one liners functions
Author: Bruno Lerner
"""

def triple(message):
    return "".join([3*x for x in message])

if __name__ == "__main__":
    print(triple('hello'))
