"""
It makes one liners functions
Author: Bruno Lerner
"""


def hex_encoder(message):
    """
    it transforms each letter in the string into its ascii value and then converts to hex
    :param message: 
    :return: 
    """

    return "".join([str(hex(ord(x)))[2:] for x in message])


if __name__ == "__main__":
    print(hex_encoder('hello world'))
