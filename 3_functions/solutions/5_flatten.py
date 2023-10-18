# Uzupełnij funkcję flatten tak, aby z listy list zwracała listę zawierającą elementy z każdej z podlist.
# Wersja trudniejsza: wykorzystaj do tego list comprehension

# Tu sposób bez list comprehension:
# def flatten(my_list: list[list[any]]) -> list[any]:
#     result: list[any] = []
#     for sublist in my_list:
#         for x in sublist:
#             result.append(x)
#     return result


def flatten(my_list: list[list[any]]) -> list[any]:
    return [x for sublist in my_list for x in sublist]


assert flatten([[1], [2, 3], [-2]]) == [1, 2, 3, -2]
assert flatten([[.2], [""], [], [4j, "python", []]]) == [.2, "", 4j, "python", []]
assert flatten([]) == []
