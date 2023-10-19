# print("Blok try-except-else-finally bez wyjątku")
try:
    print("try")  # blok kodu, w którym może zostać rzucony wyjątek
except:
    print("except")  # blok, który się wykonuje w wypadku złapania wyjątku, może być kilka takich bloków
else:
    print("else")  # blok, który się wykouje w wypadku gdy nie złapano wyjątku
finally:
    print("finally")  # blok, który zawsze się wykonuje na zakończenie, niezależnie czy złapano wyjątek czy nie


print("Blok try-except-else-finally z rzuconym łapanym wyjątkiem")
try:
    print("try")  # blok kodu, w którym może zostać rzucony wyjątek
    raise EOFError()
except:
    print("except")  # blok, który się wykonuje w wypadku złapania wyjątku, może być kilka takich bloków
else:
    print("else")  # blok, który się wykouje w wypadku gdy nie złapano wyjątku
finally:
    print("finally")  # blok, który zawsze się wykonuje na zakończenie, niezależnie czy złapano wyjątek czy nie


try:
    raise ValueError
except ValueError as e:
    print(e)

try:
    raise ValueError("Message")
except ValueError as e:
    print(e)

try:
    result = 10 / 0
except Exception as e:
    print("An error occurred:", str(e))

try:
    result = 10 / 0
except (ZeroDivisionError, IOError) as e:
    print("Nie dziel przez 0!")


try:
    result = 10 / 0
except IOError as e:
    print(e)
except ZeroDivisionError as e:
    print("Nie dziel przez 0!")



class TrainingError(Exception):
    pass


# raise TrainingError("Not enough exceptions")


def exception_raiser():
    raise TrainingError("Not enough exceptions")

exception_raiser()
