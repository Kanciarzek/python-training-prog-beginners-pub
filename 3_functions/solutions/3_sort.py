# Zmodyfikuj argument key metody sort tak, aby uzyskać posortowaną listę pod względem:
# a) długości słowa
# b) liczby samogłosek
words: list[str] = ["cucumber", "brrrr", "python", "bird"]
words.sort(key=len)
assert words == ['bird', 'brrrr', 'python', 'cucumber']
# words.sort(key=lambda word: len([char for char in word if char in "aeiouy"]))
words.sort(key=lambda word: sum(1 for char in word if char in "aeiouy"))
assert words == ['brrrr', 'bird', 'python', 'cucumber']
