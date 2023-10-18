# Napisz funkcję rekurencyjnie, która zwraca n-ty wyraz ciągu fibonacciego (jest to ciąg, którego każdy wyraz,
# to suma dwóch poprzednich, przy czym pierwszyszy i drugi wyraz to 1).
# Kolejne wyrazy tego ciągu, to: 1, 1, 2 (bo 1+1=2), 3 (bo 2+1=3), 5 (bo 2+3=5) itd.
# Wersja rozbudowana: Przetestuj dekorator cache z modułu functools i porównaj czasy wykonania z nim i bez niego.

from functools import cache

import timeit


def fibonacci(n: int) -> int:
    if n in [1, 2]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def fibonacci_cached(n: int) -> int:
    if n in [1, 2]:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


print(timeit.timeit(lambda: fibonacci(10)))
print(timeit.timeit(lambda: fibonacci_cached(10)))
