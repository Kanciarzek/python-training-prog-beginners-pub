# Zmodyfikuj argument key metody sort tak, aby uzyskać posortowaną listę pod względem:
# a) długości słowa
# b) liczby samogłosek
words: list[str] = ["cucumber", "brrrr", "python", "bird"]
words.sort(key=None)  # a)
assert words == ["bird", "brrrr", "python", "cucumber"]
words.sort(key=None)  # b)
assert words == ["brrrr", "bird", "python", "cucumber"]
