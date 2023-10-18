# Mamy funkcję read_all_files, która przyjmuje listę nazw plików i zwraca listę linii występujących we kolejno
# wszytskich plikach.
# Rozszerz ją następująco:
# Funkcja przyjmuje dodatkowy opcjonalny argument typu bool ignore_errors. Gdy wartość tego argumentu jest True, to funkcja pomija
# nieistniejące pliki.


def read_all_files(filenames: list[str]) -> list[str]:
    lines = []
    for filename in filenames:
        with open(filename, "r") as file:
            lines.extend(file.readlines())
    return lines


assert read_all_files([]) == []
assert read_all_files(["a.txt", "b.txt"]) == ['hakuna matata\n', 'no woman no cry\n', 'cucumber\n', 'python is awesome\n', 'no woman no cry\n', 'cucumber\n', 'python is awesome\n', 'hakuna\n', 'matata\n', 'no woman no cry\n', 'lets cry\n', 'cucumber']
# print(read_all_files(["a.txt", "b.txt", "c.txt"])) # rzuci wyjątek
assert read_all_files(["a.txt", "b.txt", "t.txt"], ignore_errors=True) == ['hakuna matata\n', 'no woman no cry\n', 'cucumber\n', 'python is awesome\n', 'no woman no cry\n', 'cucumber\n', 'python is awesome\n', 'hakuna\n', 'matata\n', 'no woman no cry\n', 'lets cry\n', 'cucumber']
assert read_all_files(["t.txt"], ignore_errors=True) == []



