### PLIK 1.13.py: Kompletny program obliczający łączną wartość wszystkich towarów dostępnych w sklepie.
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]  # Ceny 10 produktów.
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]  # Liczba sztuk każdego produktu w magazynie.

total_value = 0.0  # Łączna wartość towarów.
for i in range(len(product_prices)):  # Przechodzimy przez wszystkie produkty.
    total_value += product_prices[i] * product_quantities[i]  # Dodajemy wartość danego towaru (cena * ilość).

print(f"Total value of goods in store: {total_value:.2f}")  # Wypisujemy całkowitą wartość towaru w sklepie.
