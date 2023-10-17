# krotki (ang. tuples) - niemodyfikowalna struktura danych, z elementami o określonej kolejności

names: tuple[str, str, str, int] = ("Ania", "Jacek", "Agatka", 10)

another_names = ("Marek",)

# names[1] = 3 # to nie zadziała

all_names: tuple = names + another_names
print("all_names=", all_names)
print("all_names[:2]=", all_names[:2])

print(list(names))

for element in names:
    print(element)
