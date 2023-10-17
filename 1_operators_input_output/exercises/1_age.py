# Napisz program, który wczytuje od użytkownika rok urodzenia. Jeżeli wiek użytkownika mieści się wynosi co najmniej
# age_min i co najwyżej age_max, to jest wyświetlany komunikat "access granted". W przeciwnym wypadku
# użytkownik otrzymuje komunikat "access denied".

from datetime import date

age_min: int = 18
age_max: int = 120

current_year: int = date.today().year

