"""
It makes one liners functions
Author: Bruno Lerner
"""
URL = 'https://www.welovepython.com/onelinerexercise?python=-3.56%2C-2.55&is=-2.75%2C-4.92&awesome=-4.63%2C4.12&I=-5.75%2C-3.45&am=-1.0%2C-8.31&telling=-7.38%2C-2.41&you=-3.5%2C-3.6&but=-4.38%2C-2.92&you=-7.13%2C-6.0&can=1.63%2C-2.36&probably=-5.75%2C-6.51&see=-3.25%2C-3.64&that=1.75%2C-2.15&for=-3.75%2C5.08&name=yourself&ec=-4.88&soc=-2.05'
SEPARATOR = "%2C"
EQUAL = "="


def jsoner(url):
    """
    It gets an url and transforms it into a json
    :param url: 
    :return: 
    """

    return {x[:x.index(EQUAL)] if x.index(SEPARATOR) != -1 else x[x.index(EQUAL) + 1:]: {
        'interesting': x[x.index(EQUAL) + 1:x.index(SEPARATOR)] if x.index(SEPARATOR) != -1 else y[
                                                                                                 y.index(
                                                                                                     EQUAL):],
        'value': x[x.index("C") + 1:] if x.index(SEPARATOR) != -1 else z[z.index(EQUAL):]} for (x, y, z)
        in zip(url[url.index('?') + 1:].split("&"), url[url.index('?') + 1:].split("&")[1:] + [0],
               url[url.index('?') + 1:].split("&")[1:] + [0] + [1])}


if __name__ == "__main__":
    print(jsoner(URL))
