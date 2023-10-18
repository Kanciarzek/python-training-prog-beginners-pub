# W module os znajduje się obiekt environ, który zachowuje się, jak słownik i zawiera zmienne środowiskowe systemu
# operacyjnego. Napisz program, który:
# a) wyświetli, ile mamy zmiennych środowiskowych zaczynających się od PYTHONTRAINING_
# b) wyświetli wartość zmiennej środowiskowej PYTHONTRAINING_SECRET, a w wypadku, gdy nie jest
# ustawiona, to wypisze komunikat o tym, że należy taką zmienną ustawić.

import os

print(type(os.environ))  # de facto to nie jest zmienna typu słownikowego
print(dict(os.environ))  # ale jak bardzo chcemy, to możemy skonwertować

environmental_variables: list[str] = list(os.environ.keys())
prefix: str = "PYTHONTRAINING_"
counter: int = 0
for environmental_variable in environmental_variables:
    # if environmental_variable.startswith(prefix):
    #     counter += 1
    if environmental_variable[:len(prefix)] == prefix:
        counter += 1

print(f"Mamy {counter} zmiennych środowiskowych zaczynających się od {prefix}")


python_secret = os.environ.get("PYTHONTRAINING_SECRET")
if python_secret is None:
    print("Brak zmienniej środowiskowej PYTHONTRAINING_SECRET. Ustaw ją przed ponownym uruchomieniem programu.")
else:
    print(python_secret)
