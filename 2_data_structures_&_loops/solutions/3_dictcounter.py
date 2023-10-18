# Napisz kod, stworzy słownik, którego kluczami będą elementy poniższej listy, a wartością, ile razy dany elementy
# występuje w liście.
numbers: list[int] = [2, 5, 1, 5, 3, 5, 1, 25, -3]

counter: dict[int, int] = dict()
for number in numbers:
    if number in counter.keys():
        counter[number] += 1
    else:
        counter[number] = 1

for key, value in counter.items():
    print(f"W liście element {key} znalazł się {value} raz(y)")
    # print(f"W liście element {key} znalazł się {value} raz{'y' if value > 1 else ''}")

from collections import defaultdict

counter: dict[int, int] = defaultdict(lambda: 1)
for number in numbers:
    counter[number] += 1

print(counter)

from collections import Counter

print(Counter(numbers))
