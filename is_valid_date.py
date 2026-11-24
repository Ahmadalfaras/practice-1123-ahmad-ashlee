from days_in_month import days_in_month


def is_valid_date(year: int, month: int, day: int) -> bool:
	if year < 1 or not 1 <= month <= 12:
		return False
	return 1 <= day <= days_in_month(year, month)
