# Uzupełnij funkcję flatten tak, aby z listy list zwracała listę zawierającą elementy z każdej z podlist.
# Wersja trudniejsza: wykorzystaj do tego list comprehension

def flatten(my_list: list[list[any]]) -> list[any]:
    pass


assert flatten([[1], [2, 3], [-2]]) == [1, 2, 3, -2]
assert flatten([[.2], [""], [], [4j, "python", []]]) == [.2, "", 4j, "python", []]
assert flatten([]) == []
