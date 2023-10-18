# comprehensions
numbers: list[int] = [5, 3, 12, -5, 4, -4]

numbers_squared = []
for number in numbers:
    numbers_squared.append(number ** 2)

print(numbers_squared)

# Można to zrobić jako list comprehension
print([x ** 2 for x in numbers])
# Są też odpowiedniki:
# set comprehension
print({x ** 2 for x in numbers})
# dict comprehension
print({x: x + 1 for x in numbers})


numbers_squared_less_than_10 = []
for number in numbers:
    if number < 10:
        numbers_squared_less_than_10.append(number ** 2)
print(numbers_squared_less_than_10)

# Można też zrobić filtrowanie używając list comprehension
print([x ** 2 for x in numbers if x < 10])

print([x for x in numbers if x < 10])
def my_filter(x):
    return x < 10

# Jednak gdy zależy nam tylko na filtrowaniu można użyć metody filter
print(list(filter(my_filter, numbers)))
print(list(filter(lambda x: x < 10, numbers)))

print(filter(lambda x: x < 10, numbers))  # zwróci filer object
print([filter(lambda x: x < 10, numbers)])  # zwróci listę jednoemelentową zaiwerającą filter object

# Zagnieżdżone list comprehension
print([(x, y) for x in [1, 2, 3] for y in [4, 5]])

print("== break ==")

values: list[int] = [1, 2, 5, 2, 11]
threshold: int = 4

# is_threshold_reached: bool = False
# for value in values:
#     if value >= threshold:
#         is_threshold_reached = True
#
# if not is_threshold_reached:
#     print("Próg nie został osiągięty")
# else:
#     print("Próg został osiągnięty")

is_threshold_reached: bool = False
for value in values:
    if value >= threshold:
        is_threshold_reached = True
        print("Próg został osiągnięty")
        break
if not is_threshold_reached:
    print("Próg nie został osiągięty")


print(" == Continue ==")

for i in range(10):
    if i % 2 == 0:
        print(i)


for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

print("== any() oraz all() ==")

# any() oraz all()
list_of_bool_values: list[bool] = [True, False, "test".islower()]
list_contains_any_true_boolean: bool = False
for value in list_of_bool_values:
    if value is True:
        list_contains_any_true_boolean = True

print(list_contains_any_true_boolean)
print(any(list_of_bool_values))

list_contains_only_true_booleans: bool = True
for value in list_of_bool_values:
    if value is False:
        list_contains_only_true_booleans = False

print(list_contains_only_true_booleans)

print(all(list_of_bool_values))


values: list[int] = [1, 2, 5, 2, 11]
threshold: int = 4
print(all(x >= threshold for x in values))
