"""
It makes one liners functions
Author: Bruno Lerner
"""


def hex_decoder(message):
    '''
    It gets letters in the string 2 by 2, and transforms them into their decimal value
    :param message:
    :return:
    '''
    return "".join([chr(int(message[int(ind)] + message[int(ind + 1)], 16)) for ind, x in enumerate(message) if int(ind) % 2 == 0])


if __name__ == "__main__":
    print(hex_decoder('68656c6c6f20776f726c64'))
