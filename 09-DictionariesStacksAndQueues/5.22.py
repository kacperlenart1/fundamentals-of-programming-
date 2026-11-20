import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.22.py: Program pobierający dane o produkcie (str, float, bool) i zapisujący je do product.json.
import json  # Importujemy moduł json.

product = {}  # Pusty słownik opisujący produkt.

name = input("Enter product name: ").strip()  # Nazwa jako napis (str).
price = round(float(input("Enter product price: ")), 2)  # Cena jako liczba zmiennoprzecinkowa (float).
paid_input = input("Is it paid? (yes/no): ").strip().lower()  # Status płatności jako napis do konwersji na bool.
paid = paid_input in {"yes", "y", "true", "1"}  # Konwertujemy odpowiedź na wartość logiczną (bool).

product["name"] = name  # Zapisujemy nazwę produktu.
product["price"] = price  # Zapisujemy cenę produktu.
product["paid"] = paid  # Zapisujemy informację o opłaceniu.

with open("product.json", "w", encoding="utf-8") as file:  # Otwieramy product.json do zapisu.
    json.dump(product, file, indent=4, ensure_ascii=False)  # Zapisujemy słownik do pliku JSON.

print("Saved product to product.json")  # Potwierdzamy zapis.
