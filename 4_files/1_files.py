# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)

from typing import TextIO

file: TextIO = open("example_text.txt", "r")
for line in file:
    print(line.strip())  # strip usuwa białe znaki z końców
file.close()

# context manager
with open("example_text.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip usuwa białe znaki z końców
    # file.write("test")  # rzuci wyjątkiem, bo plik jest otwarty w trybie do odczytu

# file.readline()  # rzuci wyjątkiem, bo plik już zamknięty

# tryb bajtowy
with open("example_text.txt", "rb") as file:
    file_content: bytes = file.read()
    print(file_content)
    print(type(file_content))
    print(file_content[0])

with open("polish_letters.txt", "r") as file:
    for line in file:
        print(line.strip())  # coś tu nie gra, używane jest domyślne enkodowanie windows-1250

with open("polish_letters.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # już lepiej

with open("example_text.txt", "r", encoding="utf-8") as input_file:
    with open("result.txt", "w") as output_file:
        for line in input_file:
            output_file.write(line.upper())

# Możemy otworzyć kilka plików w contex managerze
# with (open("example_text.txt", "r", encoding="utf-8") as input_file,
#       open("result.txt", "w") as output_file):
#     for line in input_file:
#         output_file.write(line.upper())

# moduł os
import os

print(os.path.isfile("b.txt"))  # czy jest plikiem
print(os.path.exists("b.txt"))  # czy ścieżka istnieje
print(os.path.isdir("b.txt"))  # czy jest katalogiem
print(os.path.isfile("exercises"))
print(os.path.exists("exercises"))
print(os.path.isdir("exercises"))
