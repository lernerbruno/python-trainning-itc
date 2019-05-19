"""
Author: Bruno Lerner
"""


def main():
    # It gets the countries list and transform each country to be in a title format
    world_map = lambda countries: list(map(lambda country: country.title(), countries))
    print(world_map(['bRaSiL', 'Israel', 'france']))

if __name__ == "__main__":
    main()
