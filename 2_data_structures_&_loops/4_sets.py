# zbiór (ang. set) - modyfikowalna, nieuporządkowana struktura danych

numbers: list[int] = [44, 55, 66, 44, 70, 44]
numbers_set: set[int] = set(numbers)
print(numbers_set)

numbers_set = {55, 77, 128, 55}
print(numbers_set)

for numbers in numbers_set:
    print(numbers)
numbers_set.add(5)
print(numbers_set)

numbers_set2: set[int] = {55, 77, 15, -4}

print(numbers_set2)
print(numbers_set | numbers_set2)  # suma zbiorów
print(numbers_set & numbers_set2)  # cześć wspólna zbiorów
print(numbers_set - numbers_set2)  # różnica zbiorów
print(numbers_set.difference(numbers_set2))  # różnica zbiorów

