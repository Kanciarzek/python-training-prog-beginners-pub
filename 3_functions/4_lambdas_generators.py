import time
import timeit
from functools import cache

add = lambda a, b: a + b

print(add(1, 2))

# jest to równoważne:
def add(a, b):
    return a + b

print(add(1, 2))


my_list = [("Jacek", 5), ("Agata", 13), ("Ilona", 6)]
print(max(my_list))
print(max(my_list, key=lambda x: x[1]))  # wyrażenia lambda są przydatne tam, gdzie trzeba podać funckję jako argument
print(sorted(my_list, key=lambda x: x[1]))


def infinite_natural_numbers_generator(start: int):
    while True:
        yield start
        start += 1

generator = infinite_natural_numbers_generator(5)
print(next(generator))
print(next(generator))
# print(list(infinite_natural_numbers_generator(1))) # to się nie zakończy

def limited_natural_numbers_generator(start: int, end: int):
    while start < end:
        yield start
        start += 1

generator = infinite_natural_numbers_generator(5)
print(next(generator))
print(next(generator))
print("Limited generator in loop")
for x in limited_natural_numbers_generator(5, 10):
    print(x)


# rekurencja

def factorial(n: int) -> int: #silnia
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(10))


def long_sleep(n: int) -> int:
    time.sleep(n)
    return n

print("Uruchamiamy funkcję")
print(long_sleep(2))


@cache
def long_sleep_cached(n: int) -> int:
    time.sleep(n)
    return n


print("Pierwsze uruchomienie")
print(long_sleep_cached(2))
print("To powino być w cache")
print(long_sleep_cached(2))
print("Uruchamiamy dla 3")
print(long_sleep_cached(3))
print(long_sleep_cached.cache_info())

print("Porównanie czasów")

print(timeit.timeit(lambda: long_sleep(2), number=1)) # zwraca czas w senkundach, ile zajęło wywołanie funkcji
print(timeit.timeit(lambda: long_sleep_cached(2), number=1))
