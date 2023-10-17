# listy
import datetime
from datetime import date
from typing import List

# type hint dla list "w starym stylu"
training_attendants: List[str] = ["Jacek", "Grzegorz", "Marcin"]
print(training_attendants)
print(type(training_attendants))
print(training_attendants[0])
training_attendants[0] = "Jarek"
print(training_attendants)
# print(training_attendants[50]) # brak elementu o podenym indeksie

print(training_attendants[-1])  # za pomocą ujemnych wartości możemy pobierać wartości od końca
print(training_attendants[-2])  # za pomocą ujemnych wartości możemy pobierać wartości od końca
print("python"[-1])

# Typehint od Python 3.9
numbers: list[int] = [1, 15, -3, 10, 100, 78]

rubbish: list[any] = [1, 5, "string", 3.5, datetime.date.today()]
print(rubbish)

# slicing
print(numbers[:3])  # elementy o indeksach 0, 1, 2
print(numbers[:1000])  # to zadziała pomimo, że długość listy jest < 1000, zwróci kopię listy
print(numbers[3:])  # elementy o indeksach 3, 4 itd.
print(numbers[1:3])
print(numbers[1:5:2])  # od elementu o indeksie 1 do elementu o indeksie 5 (bez tego elementu) co 2 element
print(numbers[1::2])  # od elementu o indeksie 1 do końca co 2 element
print(numbers[::2])  # co 2 element
print(numbers[::-1])  # zwróci listę z elementami w odwrotnej kolejności

print("Bez copy")

new_numbers: list[int] = numbers
new_numbers[2] = -777
print(numbers)
print(new_numbers)
numbers[2] = -3

print(numbers)
print(new_numbers)

print("Z użyciem copy:")

print(numbers)
print(new_numbers)

new_numbers: list[int] = numbers.copy()
new_numbers[2] = -777
print(numbers)
print(new_numbers)

new_numbers[2] = -3

print("Slicing:")
new_numbers_shortened = numbers[:5]
new_numbers_shortened[2] = 2000
print(numbers)
print(new_numbers_shortened)

print("List of lists:")
list_of_lists: list[list[int]] = [[1, 2], [3, 4]]
new_list_of_lists: list[list[int]] = list_of_lists
print(list_of_lists)
print(list_of_lists)

print("Bez copy:")
new_list_of_lists[1][1] = 100
print(list_of_lists)
print(new_list_of_lists)
new_list_of_lists[1][1] = 4

print("Z użyciem copy:")
list_of_lists: list[list[int]] = [[1, 2], [3, 4]]
new_list_of_lists: list[list[int]] = list_of_lists.copy()
print(list_of_lists)
print(new_list_of_lists)
new_list_of_lists[1][1] = 100
print(list_of_lists)
print(new_list_of_lists)

print("Z użyciem deepcopy:")
from copy import deepcopy

list_of_lists: list[list[int]] = [[1, 2], [3, 4]]
new_list_of_lists: list[list[int]] = deepcopy(list_of_lists)
print(list_of_lists)
print(new_list_of_lists)
new_list_of_lists[1][1] = 100
print(list_of_lists)
print(new_list_of_lists)

print("Dodatkowe operacje na listach:")

my_list: list[int] = [1, 2, 5, -3]

my_list.remove(5)  # usunie element z listy podany jako argument
print(my_list)

del my_list[0]
print(my_list)

empty_list = []

if empty_list:
    print("empty_list jest konwertowane do True")
else:
    print("empty_list jest konwertowane do False")

# preferowane testowane, czy lista jest pusta
if len(empty_list) != 0:
    print("empty_list jest konwertowane do True")
else:
    print("empty_list jest konwertowane do False")

