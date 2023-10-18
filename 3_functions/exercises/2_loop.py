# Mamy tutaj 2 przykłady kodu z pętlą.
# Zmodyfikuj je tak, aby zastąpić ją odpowiednim wyrażeniem, jak np. list comprehension.
# Pierwszy fragment
from datetime import date

words: list[str] = ["python", "SnAkE", "function"]
i: int = 0
upper_case_words = []
while i < len(words):
    upper_case_words.append(words[i].upper())
    i += 1
print(upper_case_words)

# Drugi fragment
dates: list[date] = [date(2010, 10, 5), date(2010, 10, 6), date(2023, 10, 14)]
is_any_saturday: bool = False
for date in dates:
    if date.weekday() == 5:
        is_any_saturday = True
print("is_any_saturday =", is_any_saturday)
