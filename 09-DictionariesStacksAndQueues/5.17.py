import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.17.py: Program wczytujący listę miast z cities.json i wypisujący informacje o każdym mieście.
import json  # Importujemy moduł json.

with open("cities.json", "r", encoding="utf-8") as file:  # Otwieramy cities.json z kodowaniem UTF-8 (polskie znaki).
    data = json.load(file)  # Wczytujemy listę słowników z danymi miast.

for city in data:  # Przechodzimy przez każde miasto w liście.
    for key, value in city.items():  # Przechodzimy przez pola pojedynczego miasta.
        print(f"{key} : {value}")  # Wypisujemy pole i jego wartość.
    print()  # Oddzielamy kolejne miasta pustą linią.
