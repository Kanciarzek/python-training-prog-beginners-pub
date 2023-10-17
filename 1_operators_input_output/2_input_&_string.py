# Checmey napisać program, który pobiera od użytkownika 2 liczby i wypisuje ich sumę

# Pierwsza wersja
# x = input("Podaj pierwszą liczbę:")
# y = input("Podaj drugą liczbę:")
#
# print("x + y =", x + y)  # raczej nie o to chodziło, zajdzie konkatenacja stringów
# print(x)
# print(y)
# print(type(x))

# Druga wersja

# x = int(input("Podaj pierwszą liczbę:"))
# y = int(input("Podaj drugą liczbę:"))
#
# print("x + y =", x + y)  # teraz się zgadza
#
# print(int("10"))  # konwertujemy str na typ int


# Trzecia wersja

# x = float(input("Podaj pierwszą liczbę:"))
# y = float(input("Podaj drugą liczbę:"))
#
# print("x + y =", x + y)  # teraz się zgadza
#
# print(float("10"))  # konwertujemy str na typ float

# Dzielenie
#
# x = float(input("Podaj pierwszą liczbę:"))
# y = float(input("Podaj drugą liczbę:"))
#
# print("x / y =", x / y) # dla np. 100/7 wypisze dużo cyfr po przecinku

# Formatowanie wartości

x = float(input("Podaj pierwszą liczbę:"))
y = float(input("Podaj drugą liczbę:"))

result: float = x / y

print(f"{x}/{y} = {result:.3f}")  # f-string (dostępny od pythona 3.6)
print("{}/{} = {:.3f}".format(x,y,result))  # metoda format typu string - alternatywny sposób


