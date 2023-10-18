# Napisz funkcję, która przyjmuje nieskończoną liczbę argumentów typu str i zwraca ich je wszystkie połączone
# Wersja rozbudowana:
# Funkcja przyjmuje dodatkowy argument limit, Funkcja ma połączyć tyle argumentów, aby długość wynikowa nie
# przekroczyła limit.

def join_strings() -> str:
    pass

assert join_strings("test", "test2") == "testtest2"
assert join_strings() == ""
assert join_strings("Hakuna", "Matata", "cucumber", limit=15) == "HakunaMatata"
assert join_strings("Hakuna", "Matata", "cucumber", "", limit=100) == "HakunaMatatacucumber"
