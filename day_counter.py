import sys
from datetime import date

from is_valid_date import is_valid_date


def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    if not is_valid_date(year1, month1, day1) or not is_valid_date(year2, month2, day2):
        raise ValueError("invalid date")
    return abs((date(year2, month2, day2) - date(year1, month1, day1)).days)


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python3 day_counter.py <year1> <month1> <day1> <year2> <month2> <day2>")
        sys.exit(1)
    try:
        print(day_counter(*[int(arg) for arg in sys.argv[1:]]))
    except ValueError:
        print("Those are not valid dates.")
        sys.exit(1)
