"""
It makes one liners functions
Author: Bruno Lerner
"""
URL = 'https://www.welovepython.com/onelinerexercise?python=-3.56%2C-2.55&is=-2.75%2C-4.92&awesome=-4.63%2C4.12&I=-5.75%2C-3.45&am=-1.0%2C-8.31&telling=-7.38%2C-2.41&you=-3.5%2C-3.6&but=-4.38%2C-2.92&you=-7.13%2C-6.0&can=1.63%2C-2.36&probably=-5.75%2C-6.51&see=-3.25%2C-3.64&that=1.75%2C-2.15&for=-3.75%2C5.08'

def jsoner(url):
    '''
    It gets an url and transforms it into a json
    :param message:
    :return:
    '''
    return {x[:x.index('=')]: {'interesting': x[x.index("=") + 1:x.index("%2C")], 'value': x[x.index("C") + 1:]} for x in url[url.index('?') + 1:].split("&")}

if __name__ == "__main__":
    print(jsoner(URL))
