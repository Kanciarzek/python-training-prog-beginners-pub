from typing import Callable


# Bez type hint funkcja wyglądałaby tak: def myfunction():
def my_function() -> None:
    pass


print(my_function())  # Wypisze None


# Bez type hint funkcja zaczynałaby się tak: def divide(arg):
def divide(arg: int) -> int:
    return arg // 2


print(divide(2))
print(divide(7))
# divide("test") to nie zadziała


# Ta metoda przesłoni nam poprzednią
def divide(arg: str) -> str:
    return arg[:len(arg) // 2]


# divide(2)
# divide(7)
# divide("test")


# Można albo użyć funkcji o osobnej nazwie, albo rozwiązać to w ten sposób:
def divide(arg: int | str) -> int | str:
    if isinstance(arg, int):
        return arg // 2
    elif isinstance(arg, str):
        return arg[:len(arg) // 2]



print(divide(2))
print(divide("test"))

#
def add(a: int,b: int):
    return a + b


print(add(1,5))
print(add("a","b"))  # typehint nie modyfikuje działania funkcji, zadziała to też dla typu str

# Domyślny argument
def divide(arg: int | str, divider: int = 3) -> int | str:
    if isinstance(arg, int):
        return arg // divider
    elif isinstance(arg, str):
        return arg[:len(arg) // divider]


print(divide(150))
print(divide(150, 5))
print(divide(150, divider=3))  # keyword arguments - na końcu listy argumentów
print(divide(divider=3, arg=150))  # keyword arguments możemy podawać w dowolnej kolejności
print(divide(arg="test"))
arg_list = [150, 3]
print(divide(*arg_list))  # możemy w ten sposób "odpakować" (unpack) wartości z listy i przekazać je jako argumenty


# Domyślny argument zainicjalizuje się tylko raz
def list_updater(my_list: list = []) -> list:
    my_list.append("surprise")
    return my_list


print(list_updater())
print(list_updater())
print(list_updater())


# Co PyCharm sugeruje, żeby sobie z tym poradzić:
def list_updater(my_list=None) -> list:
    if my_list is None:
        my_list = []
    my_list.append("surprise")
    return my_list

print(list_updater())
print(list_updater())
print(list_updater())


# Nieskończenie wiele argumentów
def infinite_arguments(*args) -> None:
    print(args)
    print(type(args))  # tuple


infinite_arguments(1, 2, 3)

def infinite_arguments(first, *args) -> None:
    print(first)
    print(args)
    print(type(args))  # tuple


infinite_arguments(1, 2, 3)


def mean_counter(*args):
    return sum(args) / len(args)


print(mean_counter(10, 20, 33))


def keyword_arguments(**kwargs) -> None:
    print(kwargs)
    print(type(kwargs)) # dict


keyword_arguments(arg1=5, arg2=10)

def keyword_arguments(arg2, **kwargs) -> None:
    print(kwargs)
    print(type(kwargs))  # dict


keyword_arguments(arg1=5, arg2=10)


# funkcje, które zwracają funkcje

def function_adder(value: int = 2) -> Callable[[int], int]:
    def result(arg: int) -> int:
        return arg + value

    return result


add_two = function_adder()
print(add_two(14))

add_three = function_adder(3)
print(add_three(14))
print(function_adder()(14))

# Zasięg zmiennych w funkcji

variable: int = 10


def print_variable() -> None:
    print(variable)


print_variable()


def print_variable() -> None:
    variable = 15
    print(variable)


print_variable()


def modify_variable() -> None:
    global variable  # Bez tego utworzy się lokalna zmienna variable
    variable = 1


modify_variable()
print(variable)
