# Napisz kod, który usunie z podanej listy duplikaty. Czy możesz to zrobić tak, żeby zachowana była kolejność?

numbers: list[int] = [2, 5, 1, 5, 3, 5, 1, 25, -3]

print(list(set(numbers)))

numbers_without_duplicates: list[int] = []
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)

print(numbers_without_duplicates)
