def is_leap_year(year: int) -> bool:
    # Gregorian rule: divisible by 4, except centuries, unless divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
