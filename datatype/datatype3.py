def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


import calendar

calendar.isleap(0)
calendar.isleap(1)
calendar.isleap(4)
calendar.isleap(1200)
calendar.isleap(700)
calendar.isleap(2020)
