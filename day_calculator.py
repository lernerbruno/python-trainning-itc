"""
Creates a day calculator
Author: Bruno Lerner
"""
import datetime

def day_calculator(number_of_days):
    """
    It adds number of days to the current time and formats it as iso
    :param number_of_days:
    :return:
    """
    result_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    print(result_date.isoformat())


if __name__ == "__main__":
    day_calculator(5)
