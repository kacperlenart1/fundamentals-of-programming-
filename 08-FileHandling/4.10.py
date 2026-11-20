import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.10.py: Program wypisujący produkty z clothing.csv o cenie poniżej 60 i stanie magazynowym poniżej 40.
import csv  # Importujemy moduł csv.

with open("clothing.csv", "r", encoding="utf-8", newline="") as file:  # Otwieramy plik clothing.csv.
    reader = csv.DictReader(file)  # Wczytujemy wiersze jako słowniki według nagłówków kolumn.
    for row in reader:  # Przechodzimy przez każdy produkt.
        price = float(row.get("Price", 0))  # Konwertujemy cenę na liczbę zmiennoprzecinkową.
        stock = int(row.get("Stock_Quantity", 0))  # Konwertujemy stan magazynowy na liczbę całkowitą.
        if price < 60 and stock < 40:  # Sprawdzamy oba warunki (cena < 60 oraz stan < 40).
            print(row)  # Wypisujemy pasujący produkt.
