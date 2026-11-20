### PLIK 5.7.py: Program wypisujący listę hoteli, średnią cenę pokoju oraz wskazujący tańsze miasto.
hotels_in_Krakow = [  # Lista hoteli w Krakowie.
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00},
]  # Koniec listy hoteli w Krakowie.

hotels_in_Sopot = [  # Lista hoteli w Sopocie.
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00},
]  # Koniec listy hoteli w Sopocie.


def hotel_list(hotels):  # Zwraca nazwy hoteli oddzielone przecinkami.
    names = [hotel["name"] for hotel in hotels]  # Wyciągamy same nazwy hoteli.
    return ",".join(names)  # Łączymy nazwy w jeden napis rozdzielony przecinkiem.


def avg_price(hotels):  # Zwraca średnią cenę pokoju zaokrągloną do liczby całkowitej.
    total = sum(hotel["price"] for hotel in hotels)  # Sumujemy ceny wszystkich hoteli z listy.
    return round(total / len(hotels))  # Liczymy średnią i zaokrąglamy do int.


krakow_avg = avg_price(hotels_in_Krakow)  # Średnia cena w Krakowie.
sopot_avg = avg_price(hotels_in_Sopot)  # Średnia cena w Sopocie.

print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))  # Wypisujemy listę hoteli w Krakowie.
print("Average hotel price in Krakow:", krakow_avg)  # Wypisujemy średnią w Krakowie.
print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))  # Wypisujemy listę hoteli w Sopocie.
print("Average hotel price in Sopot:", sopot_avg)  # Wypisujemy średnią w Sopocie.

if krakow_avg < sopot_avg:  # Porównujemy średnie ceny między miastami.
    cheaper_in = "Krakow"  # Kraków jest tańszy.
elif sopot_avg < krakow_avg:  # Gdy Sopot ma niższą średnią.
    cheaper_in = "Sopot"  # Sopot jest tańszy.
else:  # Gdy średnie są równe.
    cheaper_in = "Both cities (equal average)"  # Równe ceny.

print("Cheaper hotels in:", cheaper_in)  # Wypisujemy, gdzie hotele są tańsze.
