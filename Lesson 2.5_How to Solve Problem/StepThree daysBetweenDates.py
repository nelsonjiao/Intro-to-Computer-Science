def daysBetweenDates():
	days = 0
	while dateIsBefore:
		year1, month1, day1 = nextDay()
		days += 1
	return days