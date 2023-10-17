training_attendants: list[str] = ["Jacek", "Grzegorz", "Marcin"]
who_passed_test: list[str] = ["Jacek", "Marcin", "Agata"]

print(who_passed_test[0] in training_attendants)
print(who_passed_test[1] in training_attendants)
print(who_passed_test[2] in training_attendants)

print("== Pętle ==")
n: int = len(who_passed_test)
i: int = 0
# pętla while
while i < n:
    attendant: str = who_passed_test[i]
    if attendant in training_attendants:
        print(f"{attendant} zaliczył test")
    else:
        print(f"{attendant} nie znajduje się na liście")
    i += 1  # w Pythonie nie ma operator inkrementacji i++

# pętla for
n = len(who_passed_test)
for i in range(n):
    attendant: str = who_passed_test[i]
    if attendant in training_attendants:
        print(f"{attendant} zaliczył test")
    else:
        print(f"{attendant} nie znajduje się na liście")

# pętla for-each
n = len(who_passed_test)
for attendant in who_passed_test:
    if attendant in training_attendants:
        print(f"{attendant} zaliczył test")
    else:
        print(f"{attendant} nie znajduje się na liście")


# for i in range(5):
#     print("Wypisz to 5 razy")

for _ in range(5):
    print("Wypisz to 5 razy")
