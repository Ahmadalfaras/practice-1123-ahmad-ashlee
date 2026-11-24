from days_in_month import days_in_month


def is_valid_date(year: int, month: int, day: int) -> bool:
    # year has to be positive, month 1-12, day within that month
    if year < 1:
        return False
    if not 1 <= month <= 12:
        return False
    if day < 1:
        return False
    return day <= days_in_month(year, month)
