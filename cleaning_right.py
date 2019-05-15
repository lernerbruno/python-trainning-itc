"""
It makes one liners functions
Author: Bruno Lerner
"""

def cleaning_right(message):
    '''
    it strips c o f and e letters from right of each word
    :param message:
    :return:
    '''
    return [x.rstrip('cofe') for x in message]

if __name__ == "__main__":
    print(cleaning_right(['hell', 'hello', 'hello worldcofofcfee']))
