# tak wyglądają komentarze
# print służy do wypisywania na standardowe wyjście
# zakomentowanie linii ctrl + /
print()  # wypisze pustą linię

print("Hello world")
print("Hello", "world")

print("Mam", 5, "złotych")
print("Mam", 5, "złotych", sep=",")  # modyfikujemy separator
print("Mam", 5, "złotych", sep="")  # wypisze złączone stringi
print("Hello world", end="")  # Nie zakończy wypisywania znakiem nowej linii
print("Hello world")

print("A tu sobie\nzłamię linię")  # \n - znak nowej linii
print("Programuję w\tPythonie")  # \t - tabulator
print("Programuję w Pythonie\\Javie")  # \\ - aby uzyskać \ w ciągu znaków

print("== Typy wbudowane ==")

a = 5
print(type(a))  # dzięki type możemy poznać typ przechowywanej wartości (tu: int)
a = "test"
print(type(a))  # mamy dynamiczne typowanie, tu typ: str
b = 2.0
print(type(b))  # typ: float
c = 4 + 5j
print(type(c))  # typ: complex
name = "Paweł"
print(type(name))
name = 'Paulina'  # możemy używać '' do definiowania wratości typu str
print(type(name))
# wielolinijkowe ciągi znaków
big_string = """Ten string
zajmuje
wiele linii"""
print(big_string)

d: int = 120  # typehint - wskazówka dla IDE odnośnie typu przechowywanej wartości
d = "string"  # to zadziała pomimo przypisania wartości typu str
print(d)

is_earth_flat: bool = False  # false nie zadziała
is_python_dynamically_typed: bool = True
print(type(True))
print(type(is_python_dynamically_typed))  # typ logiczny

print("== Operatory arytmetyczne ==")
a = 5
print("a = ", a)
print("b = ", b)
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
c = 5
print("a / c = ", a / c)  # zawsze zwróci float
print("a // 2 = ", a // 2)  # dzielenie całkowity (ile razy 2 mieści się w a)
print("5 % 2 = ", 5 % 2)  # reszta z dzielenia
print("5 ** 2 = ", 5 ** 2)  # potęgowanie
print("5 ** 1.5 = ", 5 ** 1.5)  # potęgowanie
print("5 ** 1.5j = ", 5 ** 1.5j)  # potęgowanie
print("5 >> 1 = ", 5 >> 1)  # przesunięcie bitowe w prawo
print("5 >> 2 = ", 5 >> 2)  # przesunięcie bitowe w prawo
print("5 << 2 = ", 5 << 2)  # przesunięcie bitowe w prawo
# print("5 >> 1.5", 5 >> 1.5)  # to nie zadziała
