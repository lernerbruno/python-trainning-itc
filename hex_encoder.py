"""
It makes one liners functions
Author: Bruno Lerner
"""

def hex_encoder(message):
    return "".join([str(ord(x)) for x in message])

if __name__ == "__main__":
    print(hex_encoder('aaaa'))
