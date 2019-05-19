"""
Author: Bruno Lerner
"""
R_STRIP = 'md'
L_STRIP = 'IF'


def main():
    transform_to_title = lambda countries: map(lambda country: country.title(), countries)

    # It gets the countries list and transform each country to be in a title format
    filtered_world_map = lambda countries: list(filter(
        lambda country: len(country) != len(country.rstrip(R_STRIP)) or len(country) != len(country.lstrip(L_STRIP)),
        transform_to_title(countries)))
    print(filtered_world_map(['bRaSiL', 'Israel', 'france']))


if __name__ == "__main__":
    main()
