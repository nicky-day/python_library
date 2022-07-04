import datetime

day1 = datetime.date(2019, 12, 14)
print(day1)
day2 = datetime.date(2021, 6, 5)
print(day2)
diff = day2 - day1
print(diff.days)

day3 = datetime.datetime(2020, 12, 14, 14, 10, 50)
print(day3.hour)
print(day3.minute)
print(day3.second)

day4 = datetime.date(2019, 12, 14)
time4 = datetime.time(10, 14, 50)
dt = datetime.datetime.combine(day4, time4)
print(dt)

day5 = datetime.date(2019, 12, 14)
print(day5.weekday())
print(day5.isoweekday())
