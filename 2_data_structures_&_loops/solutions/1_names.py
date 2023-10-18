# Napisz program, który dla podanej listy wypisze imiona żeńskie w kolejnych liniach (tj. zakończone na a z wyjątkiem
# imienia Kuba)

names: list[str] = ["Ania", "Jacek", "Marek", "Martyna", "Zbigniew", "Kuba", "Mariola", "Grażyna"]

for name in names:
    if name[-1] == "a" and name != "Kuba":
        print(name)
