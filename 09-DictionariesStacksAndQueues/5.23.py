import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.23.py: Program wczytujący notowania EUR z euro.json (format NBP) i wypisujący je w tabeli.
import json  # Importujemy moduł json.

with open("euro.json", "r", encoding="utf-8") as file:  # Otwieramy euro.json do odczytu.
    data = json.load(file)  # Wczytujemy odpowiedź JSON w formacie NBP.

rates = data.get("rates", [])  # Pobieramy listę notowań z klucza "rates".

print(f"{'Date':<15} {'Buying Rate':<15} {'Selling Rate'}")  # Nagłówek tabeli.
print("=" * 44)  # Linia oddzielająca.

for entry in rates:  # Przechodzimy przez każde notowanie.
    effective_date = entry.get("effectiveDate", "")  # Data notowania.
    bid = entry.get("bid", 0.0)  # Kurs kupna (Buying Rate).
    ask = entry.get("ask", 0.0)  # Kurs sprzedaży (Selling Rate).
    print(f"{effective_date:<15} {bid:<15.4f} {ask:.4f}")  # Wypisujemy wiersz tabeli.
