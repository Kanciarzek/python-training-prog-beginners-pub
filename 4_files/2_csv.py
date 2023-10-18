with open("airtravel.csv", "r") as file:
    for line in file:
        print(line.strip().split(","))

import numpy as np

print(np.array([[1, 2], [3, 4]]))
print(np.array([[1, 2], [3, 4]]) + 1)
print(np.array([[1, 2], [3, 4]]).mean())
print(np.array([[1, 2], [3, 4]]).mean(axis=0))  # zwróci np.ndarray w przehowujący średnią z kolumn

data: np.ndarray = np.genfromtxt("airtravel.csv", dtype=None, encoding="utf-8", delimiter=',', skip_header=1,
                                 usecols=[1, 2, 3])
# print(data)
# print(data[:2])
# print(data[:, 1:3])
print(data[:2, 1:3])

import pandas as pd

data_df: pd.DataFrame = pd.read_csv("airtravel.csv").set_index("Month")
print(data_df)
print(data_df.columns)
print(data_df.loc["JAN"])  # bierzemy wiersz po indeksie (w tym wypadku Month)
print(data_df.iloc[0])  # berzemy wiersz po indeksie numerycznym
print(data_df.iloc[0:2])  # działa tu też slicing
print(data_df["1960"] - data_df["1959"])
print(data_df["1960"].mean())
data_df["difference"] = data_df["1960"] - data_df["1959"]  # możemy dodawać nowe kolumny do dataframe
print(data_df)
