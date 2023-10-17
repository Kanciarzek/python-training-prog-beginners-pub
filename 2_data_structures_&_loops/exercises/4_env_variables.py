# W module os znajduje się obiekt environ, który zachowuje się, jak słownik i zawiera zmienne środowiskowe systemu
# operacyjnego. Napisz program, który:
# a) wyświetli, ile mamy zmiennych środowiskowych zaczynających się od PYTHONTRAINING_
# b) wyświetli wartość zmiennej środowiskowej PYTHONTRAINING_SECRET, a w wypadku, gdy nie jest
# ustawiona, to wypisze komunikat o tym, że należy taką zmienną ustawić.

import os

print(type(os.environ))  # de facto to nie jest zmienna typu słownikowego
print(dict(os.environ))  # ale jak bardzo chcemy, to możemy skonwertować
