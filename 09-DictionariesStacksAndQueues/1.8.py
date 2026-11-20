### PLIK 1.8.py: Program obliczający wartość towarów przed i po 10% rabacie oraz aktualizujący cennik.
price_list = {  # Słownik produkt -> cena przed rabatem.
    "T-shirt": 19.99,
    "Jeans": 49.99,
    "Jacket": 89.99,
    "Sneakers": 59.99,
    "Hat": 15.99,
}  # Koniec cennika.

print("Prices before discount:")  # Nagłówek cen przed obniżką.
for item, price in price_list.items():  # Przeglądamy produkty i ceny początkowe.
    print(f"{item}: {price:.2f}")  # Wypisujemy produkt i cenę.

total_before = sum(price_list.values())  # Sumujemy ceny przed rabatem.
print(f"Total value before discount: {total_before:.2f}")  # Wypisujemy wartość przed rabatem.

for item in price_list:  # Aktualizujemy każdą cenę o -10% i zaokrąglamy do 2 miejsc.
    price_list[item] = round(price_list[item] * 0.9, 2)  # Obniżamy cenę o 10%.

print("\nPrices after 10% discount:")  # Nagłówek cen po obniżce.
for item, price in price_list.items():  # Przeglądamy zaktualizowane ceny.
    print(f"{item}: {price:.2f}")  # Wypisujemy produkt i nową cenę.

total_after = round(sum(price_list.values()), 2)  # Liczymy sumę cen po rabacie.
print(f"Total value after discount: {total_after:.2f}")  # Wypisujemy wartość po rabacie.
