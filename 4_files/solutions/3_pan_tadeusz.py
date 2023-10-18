# Mamy plik z treścią Pana Tadeusza (tadzio.txt). Napisz program, który wczyta ten plik, pominie pierwszych 10
# wierszy i zliczy, ile jest sylab w każdym wierszu. Sprawdzimy, czy rzeczywiście jest napisany trzynastozgłoskowcem.
# Wersja podstawowa:
# Ilość sylab będziemy liczyć, jako ilość samogłosek
# Wersja rozszerzona:
# Ilość sylab będziemy liczyć, jako ilość samogłosek, z wyjątkiem sytuacji gdzie 'i' poprzedza inną samogłoskę, wtedy
# liczymy to jako jedną sylabę.
# Przykład: "ania" zawiera 2 sylaby, pomimo że mamy tu 3 samogłoski


vowels = "aeiouyąęó"


# def count_syllables(string: str) -> int:
#     number_of_vowels: int = len([x for x in string if x in vowels])
#     return number_of_vowels

def count_syllables(string: str) -> int:
    number_of_vowels: int = len([x for x in string if x in vowels])
    i_and_next_vowel_counter = 0
    for i in range(len(line) - 1):
        if line[i] == "i" and line[i + 1] in vowels:
            i_and_next_vowel_counter += 1
    return number_of_vowels - i_and_next_vowel_counter


syllable_counter = {}
with open("tadzio.txt", "r", encoding="utf-8") as file:
    for _ in range(10):
        file.readline()
    for line in file:
        number_of_syllables = count_syllables(line.lower())
        if number_of_syllables in syllable_counter.keys():
            syllable_counter[number_of_syllables] += 1
        else:
            syllable_counter[number_of_syllables] = 1

print(syllable_counter)
