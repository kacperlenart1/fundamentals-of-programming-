### PLIK 1.7.py: Program wypisujący produkty, ich liczby sztuk oraz łączną liczbę wszystkich produktów.
store = {  # Słownik produkt -> liczba sztuk.
    "Laptop": 15,
    "Desktop PC": 10,
    "Monitor": 25,
    "Keyboard": 50,
    "Mouse": 60,
    "External Hard Drive": 30,
    "Printer": 12,
    "Router": 20,
    "USB Flash Drive": 100,
    "Graphics Card": 8,
}  # Koniec słownika produktów.

total_products = 0  # Licznik łącznej liczby sztuk w sklepie.
for product, quantity in store.items():  # Przechodzimy przez kolejne produkty.
    print(f"{product}: {quantity}")  # Wypisujemy nazwę produktu i liczbę sztuk.
    total_products += quantity  # Dodajemy liczbę sztuk do łącznej sumy.

print("Total number of products:", total_products)  # Wypisujemy łączną liczbę produktów.
