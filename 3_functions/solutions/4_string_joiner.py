# Napisz funkcję, która przyjmuje nieskończoną liczbę argumentów typu str i zwraca ich je wszystkie połączone
# Wersja rozbudowana:
# Funkcja przyjmuje dodatkowy opcjonalny argument limit, Funkcja ma połączyć tyle argumentów, aby długość wynikowa nie
# przekroczyła limit.

# Wersja podstawowa
# def join_strings(*args) -> str:
#     result = ""
#     for string in args:
#         result += string
#     return result

def join_strings(*args, limit: int = None) -> str:
    result = ""
    if limit is None:
        for string in args:
            result += string
    else:
        for string in args:
            if limit < len(result) + len(string):
                break
            result += string
    return result


def join_strings(*args, limit: int = float('inf')) -> str:
    result = ""
    for string in args:
        if limit < len(result) + len(string):
            break
        result += string
    return result


assert join_strings("test", "test2") == "testtest2"
assert join_strings() == ""
assert join_strings("Hakuna", "Matata", "cucumber", limit=15) == "HakunaMatata"
assert join_strings("Hakuna", "Matata", "cucumber", "", limit=100) == "HakunaMatatacucumber"
