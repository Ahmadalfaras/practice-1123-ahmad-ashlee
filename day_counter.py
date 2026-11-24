import sys

from days_in_month import days_in_month
from is_leap_year import is_leap_year
from is_valid_date import is_valid_date


def days_since_start(year: int, month: int, day: int) -> int:
    # count every day from year 1, month 1, day 1 up to this date
    total = 0
    for y in range(1, year):
        total += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        total += days_in_month(year, m)
    return total + day


def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    return abs(days_since_start(year2, month2, day2) - days_since_start(year1, month1, day1))


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python3 day_counter.py <year1> <month1> <day1> <year2> <month2> <day2>")
        sys.exit(1)
    y1, m1, d1, y2, m2, d2 = [int(arg) for arg in sys.argv[1:]]
    if not is_valid_date(y1, m1, d1) or not is_valid_date(y2, m2, d2):
        print("Those are not valid dates.")
        sys.exit(1)
    print(day_counter(y1, m1, d1, y2, m2, d2))
