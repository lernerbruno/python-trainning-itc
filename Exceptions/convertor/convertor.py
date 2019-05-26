"""
It creates a new csv file from the csv that the user inputs, and it adds a column that represents the original column but in feets
Author: Bruno Lerner
"""
import argparse
import csv

NEW_FILE_FORMAT = "%s_new%s"
NUMBER_OF_COLUMNS = 1
NON_NUMERIC_ERROR = "You added a non numeric value for the meters column in row number %s. Please correct it"
NEGATIVE_NUMBER_ERROR = "You added a negative value for the meters column in row number %s . Please correct it"
COLUMN_LEN_ERROR = "The row number %s in your csv file, has more then 1 line, it has %s. Please correct it"
FILE_FORMAT_ERROR = "The file you have provided is not .csv file. Please provide a csv file"
EMPTY_FILE = "You have provided an empty file. Please provide one with data"
CSV_FORMAT = ".csv"
METER_COLUMN = 0
CONVERSION_RATE = 3.28084


def define_arguments():
    """
    Define the command line options and commands
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to the csv file", type=str)

    return parser.parse_args()


def meter_to_feet(meters):
    """
    Converts meters to feet and transform into a string
    :param meters:
    :return:
    """
    return str(CONVERSION_RATE * int(meters))


def validate_row(row, position):
    """
    For each row in the file, this function validates the len of the row, and the values inside it
    :param row:
    :param position:
    :return:
    """
    meters = row[METER_COLUMN]

    if len(row) > NUMBER_OF_COLUMNS:
        raise ValueError(COLUMN_LEN_ERROR % (str(position + 1), len(row)))
    if not meters.strip("-").isnumeric():
        raise ValueError(NON_NUMERIC_ERROR % str(position + 1))
    if int(meters) < 0:
        raise ValueError(NEGATIVE_NUMBER_ERROR % str(position + 1))

    return meters


def main():
    args = define_arguments()
    try:
        if not args.filename.endswith(CSV_FORMAT):
            raise FileExistsError(FILE_FORMAT_ERROR)

        dot_index = args.filename.index(".")
        new_filename = NEW_FILE_FORMAT % (args.filename[:dot_index], args.filename[dot_index:])

        with open(args.filename, 'r') as current_f:
            csv_reader = csv.reader(current_f)

            all_rows = []
            for i, row in enumerate(csv_reader):
                valid_meters = validate_row(row, i)
                row.append(meter_to_feet(valid_meters))
                all_rows.append(row)

        if len(all_rows) == 0:
            raise ValueError(EMPTY_FILE)
        new_f = open(new_filename, 'w')
        csv_writer = csv.writer(new_f)
        csv_writer.writerows(all_rows)

    except FileNotFoundError:
        print("The file you provided was not found. Please provide an existing one")
    except ValueError as error:
        print(error)
    except FileExistsError as error:
        print(error)


if __name__ == "__main__":
    main()
