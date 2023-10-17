# Rząd Bajtolandii, ku uciesze obywateli postanowił zorganizować loterię podatkową, która polega na
# obniżce podatku PIT losowo wybranym podatnikom. Dane wstępnie wybranych podatników znajdują się w liście
# krotek taxpayers. Krotka zawiera kolejno: NIP, imię, nazwisko, oraz pierwotną wartość podatku do zapłaty.
# Niestety, liczba miejsc w loterii jest ograniczona i jest przechowywana w max_lottery_attendants.
# Poniższy kod wykorzystuje te dane, ogranicza liczbę uczestników i wypisuje komunikat dla podatników o starej i nowej
# wartości podatku. Program działa poprawnie, gdy max_lottery_attendants jest mniejsze niż liczba podatników
# przechowywanych w taxpayers.
# Zidentyfikuj przyczynę niepoprawnego działania programu, gdy ta wartość jest większa, i zaproponuj rozwiązanie.

import random

# uzupełnij type hint dla taxpayers oraz lottery_attendants
taxpayers = [(1336, "Jacek", "Kaniecki", 1570.13),
             (2422, "Anna", "Wiśniewska", 1443.28),
             (6334, "Marcel", "Nowak", 3333.12),
             (112, "Karolina", "Szyndler", 578.13),
             (2148, "Jacek", "Doba", 112.10)]

max_lottery_attendants: int = 3  # sprawdź co się stanie, jak zwiększymy to do większej wartości jak np. 10

if len(taxpayers) <= max_lottery_attendants:
    lottery_attendants = taxpayers
else:
    lottery_attendants = taxpayers[:max_lottery_attendants]

tax_discount_percent: int = random.randint(2, 11)
print(f"Wylosowano obniżkę podatku w wysokości {tax_discount_percent}%")

for i, lottery_attendant in enumerate(lottery_attendants):
    new_tax_value: float = round(lottery_attendant[3] * (1 - tax_discount_percent / 100), 2)
    lottery_attendants[i] = lottery_attendant[:3] + (new_tax_value,)

for i in range(len(lottery_attendants)):
    print(f"Gratulujemy, {lottery_attendants[i][1]} {lottery_attendants[i][2]}! "
          f"Wylosowano Pana/Panią w loterii podatkowej! "
          f"Wcześniej podatek wynosił {taxpayers[i][3]}zł, a obecnie wynosi {lottery_attendants[i][3]}zł.")
