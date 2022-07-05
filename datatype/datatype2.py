import datetime

today = datetime.date.today()
print(today)

diff_days = datetime.timedelta(days=100)
print(diff_days)

print(today + diff_days)
print(today - diff_days)
