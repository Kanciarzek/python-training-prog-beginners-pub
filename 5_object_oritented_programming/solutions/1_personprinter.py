# Uzupełnij klasę Person tak, aby spełniała następujące warunki:
# 1. Można było stworzyć jej instancję za pomocą kontruktora przyjmującego imię, nazwisko i wiek (komentarz A)
# 2. Zawierała metodę from_string, która zwraca obiekt klasy person tworzony na podstawie argumentu typu string
# postaci: imię,nazwisko,wiek (komentarz B)
# 3. print(person) gdzie 'person' to instancja tej klasy wpisywało: "imię nazwisko, wiek" (komentarz C)
# 4. person.year_of_birth zwracało rok urodzenia tej osoby

import datetime


class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.year_of_birth = datetime.date.today().year - self.age

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age}"

    # alternatywne rozwiązanie
    # @property
    # def year_of_birth(self):
    #     return datetime.date.today().year - self.age

    @staticmethod
    def from_string(string: str):
        name, surname, age = string.split(',')
        return Person(name, surname, int(age))


data: list[str] = ["Jacek,Kowalski,18", "Anna,Nowak,35"]


people: list[Person] = [Person("Kamil", "Kaniecki", 28)] # A

for data_entry in data:
    people.append(Person.from_string(data_entry))  # B


for person in people:
    print(person)  # C
# To powinno wypisać:
# Kamil Kaniecki, 28
# Jacek Kowalski, 18
# Anna Nowak, 35

print(people[0].year_of_birth)  # D, w 2023 roku powinno wypisać 1995

