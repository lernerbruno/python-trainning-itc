"""
It makes one liners functions
Author: Bruno Lerner
"""

def space_triple(message):
    '''
    it multiplies each char of the message into 3 of itself
    :param message:
    :return:
    '''
    return " ".join([3*x for x in message.split()])

if __name__ == "__main__":
    print(space_triple('hello world'))
