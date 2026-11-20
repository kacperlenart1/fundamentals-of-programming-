import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.16.py: Program wczytujący słownik z computer.json i wypisujący wszystkie pola.
import json  # Importujemy moduł json.

with open("computer.json", "r", encoding="utf-8") as file:  # Otwieramy computer.json do odczytu.
    data = json.load(file)  # Wczytujemy zawartość JSON jako słownik.

for key, value in data.items():  # Przechodzimy przez kolejne właściwości komputera.
    print(f"{key} : {value}")  # Wypisujemy klucz i wartość.
