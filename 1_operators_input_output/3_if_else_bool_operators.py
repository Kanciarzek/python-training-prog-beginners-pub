number: int = 4
if number % 2 == 0:
    print(f"Liczba {number} jest parzysta")

number = 2

if number % 2 != 0:
    print(f"Liczba {number} jest nieparzysta")


is_python_known_by_you: bool = True
if is_python_known_by_you:
    print("Gratulacje")
    print("Więcej intrukcji w bloku")
else:
    print("Zapraszam na szkolenie")

print("==Operatory logiczne==")
print("True and False is", True and False)
print("True or False is", True or False)
print("not True is", not True)

print("== If-elif-else ==")
income_in_pln: int = 120_000
if income_in_pln < 30_000:
    tax = 0
elif income_in_pln < 120_000:
    tax = income_in_pln * 0.12 - 3_600
else:
    tax = 10_800 + (income_in_pln - 120_000) * 0.32

print(f"Podatek od dochodu {income_in_pln} wynosi: {tax}")

password: str = "very_secret"
password_length = len(password)

if password_length >= 4 and password_length <= 20:
    print("Hasło zaakceptowane")
else:
    print(f"Hasło ma długość {password_length}, a to nie jest z zakresu [4,20]")

if 4 <= password_length <= 20:  # równoważne temu, co powyżej
    print("Hasło zaakceptowane")
else:
    print(f"Hasło ma długość {password_length}, a to nie jest z zakresu [4,20]")

if 4 <= (length := len(password)) <= 20:  # assigment expression (dostępne od Pythona 3.8)
    print("Hasło zaakceptowane")
else:
    print(f"Hasło ma długość {length}, a to nie jest z zakresu [4,20]")

it_may_be_optional: int | None = None
if it_may_be_optional == None:
    print("IDE nam to oznaczy jako Warning")

if it_may_be_optional is None:
    print("IDE nam tego nie oznaczy jako Warning")

print("== Match-case ==")
print("Witaj w instalatorze programu X.")
menu_option: int = int(input("Podaj opcję 1, 2 lub 3\n"))
print(f"Wybrano opcję {menu_option}")

match menu_option:
    case 1:
        print("Instalacja programu")
    case 2:
        print("Sparwdzenie poprawności instalacji...")
    case 3:
        print("Deinstalacja programu...")
    case other:
        print(f"Nieznana opcja {other}")
    # case _:
    #     print(f"Nieznana opcja")

