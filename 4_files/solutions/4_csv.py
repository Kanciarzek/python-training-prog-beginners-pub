# Wczytaj plik data.csv zawierający dane osób. Oblicz BMI dla każdej osoby
# (masa dzielona przez wzrost_w_metrach_do_kwadratu), średnią tych wartości i wypisz je na standardowe wyjście.

import numpy as np

data: np.ndarray = np.genfromtxt("data.csv", dtype=None, delimiter=',', encoding='utf-8', skip_header=True)

bmi_ndarray: np.ndarray = data[:, 3] / (data[:, 2] / 100) ** 2

for person_id, bmi in zip(data[:, 0], bmi_ndarray):
    print(f"Osoba o id {person_id} ma bmi {bmi:.2f}")

# alternatywne rozwiązanie
# for i in range(len(bmi_ndarray)):
#     print(f"Osoba o id {data[i, 0]} ma bmi {bmi_ndarray[i]:.2f}")


print(bmi_ndarray.mean())


## alternatywne rozwiązanie

import pandas as pd

data: pd.DataFrame = pd.read_csv("data.csv", delimiter=",")
data["bmi"] = data["weight(kg)"] / (data["height(cm)"] / 100) ** 2


for person_id, bmi in zip(data["id"], data["bmi"]):
    print(f"Osoba o id {person_id} ma bmi {bmi:.2f}")

print(data["bmi"].mean())
