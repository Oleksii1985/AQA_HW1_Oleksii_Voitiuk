"""
Реализовать функцию которая возвращает дату недельной давности от текущего момента времени.
"""
from datetime import datetime, timedelta


def subtract_one_week():
    date_now = datetime.now()
    seven_days = timedelta(7)
    one_week_ago = date_now - seven_days
    return one_week_ago


if __name__ == '__main__':
    print(subtract_one_week())

# Well done
