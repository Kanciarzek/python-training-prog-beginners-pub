# Napisz program, który wczytuje od użytkownika rok urodzenia. Jeżeli wiek użytkownika mieści się wynosi co najmniej
# age_min i co najwyżej age_max, to jest wyświetlany komunikat "access granted". W przeciwnym wypadku
# użytkownik otrzymuje komunikat "access denied".

from datetime import date

age_minimal: int = 18
age_maximal: int = 120

current_year: int = date.today().year
year_of_birth: int = int(input("Put your year of birth: "))
age: int = current_year - year_of_birth

if age_minimal <= age <= age_maximal:
    print("access granted")
else:
    print("access denied")

