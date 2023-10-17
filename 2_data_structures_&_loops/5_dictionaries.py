# słownik (ang. dictionary) przechowuje pary klucz-wartość

person: dict[str, any] = dict()
print(type(person))
person["name"] = "Jacek"
person["age"] = 30
person["name"] = "Marek"
print(person)

person = {"name": "Marek", "age": 10}
print(person)

print(person["name"])
# print(person["date_of_birth"]) # nie ma takiego klucza - zostanie rzucony wyjątek

print(person.get("name"))
print(person.get("date_of_brith"))  # zwróci None
print(person.get("date_of_brith", "1970-01-01"))   # zwróci wartość podaną jako drugi argument

# Iterowanie po słowniku
print("==Iterowanie==")
for key in person:  # iterowanie po słowniku daje klucze
    print(f"{key}:{person[key]}")

for x in person.items():  # iterowanie po perosn.items() zwróci krotki (klucz, wartość)
    print(x)

for key, value in person.items():  # możemy odpadkować krotki i przypisać je do konkretnych zmiennych jej składowe
    print(f"{key}:{value}")


print({})
print(type({}))
