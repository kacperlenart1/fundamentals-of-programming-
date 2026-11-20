### PLIK 5.8.py: Program obliczający łączny koszt zakupów na podstawie słowników cen i ilości w koszyku.
prices = {"milk": 1.49, "butter": 2.09, "juice": 1.19, "bread": 1.99}  # Cennik produktów.
cart = {"juice": 3, "bread": 1, "milk": 2}  # Koszyk: produkt -> liczba sztuk.

total_cost = 0.0  # Akumulator łącznego kosztu koszyka.
for item, quantity in cart.items():  # Przechodzimy przez produkty w koszyku.
    if item in prices:  # Sprawdzamy, czy produkt ma cenę w cenniku.
        total_cost += prices[item] * quantity  # Dodajemy koszt pozycji do sumy.

print(f"Total cost: {total_cost:.2f}")  # Wypisujemy łączny koszt zakupów.
