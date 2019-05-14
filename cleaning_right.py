"""
It makes one liners functions
Author: Bruno Lerner
"""

def cleaning_right(message):
    return [x.rstrip('cofe') for x in message]

if __name__ == "__main__":
    print(cleaning_right(['hell', 'hello', 'hello worldcofofcfee']))
