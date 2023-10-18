# Napisz program, którzy otworzy plik tekstowy i wypisze kolejno wszystkie linie pomijając te puste
# Przetestuj działanie na pliku file_with_empty_lines.txt

with open("file_with_empty_lines.txt", "r") as input_file:
    for line in input_file:
        if line != "\n":
            print(line, end="")
