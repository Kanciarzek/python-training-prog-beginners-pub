# Mamy tutaj 2 przykłady kodu z pętlą.
# Zmodyfikuj je tak, aby zastąpić ją odpowiednim wyrażeniem, jak np. list comprehension.
# Pierwszy fragment
from datetime import date
words: list[str] = ["python", "SnAkE", "function"]
print([word.upper() for word in words])


# Drugi fragment
dates: list[date] = [date(2010, 10, 5), date(2010, 10, 6), date(2023, 10, 14)]
print("is_any_saturday =", any(date.weekday() == 5 for date in dates))
