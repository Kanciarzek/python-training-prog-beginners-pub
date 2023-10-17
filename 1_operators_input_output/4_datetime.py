# import datetime
from datetime import date, datetime, timedelta

# Jaki mamy dziś dzień?
print(date.today())  # data (datetime.date)
print(type(date.today()))
print(datetime.now())  # timestamp - data z godziną (datetime.datetime)
print(type(datetime.now()))
print(datetime.now().time())  # godzina (datetime.date)
print(type(datetime.now().time()))

print(date(2012, 1, 1))  # data na podstawie wartości

# Jaką datę bedziemy mieli jutro?
today: date = date.today()
# print(today + 1)  # o nie zadziała

print(date(today.year, today.month, today.day + 1))
print(today + timedelta(days=1))  # to także zadziała
# print(today + timedelta(years=1))  # to nie zadziała - można podawać do timedelta co najwyżej tygodnie

print(today.day)
print(today.month)
print(today.year)

