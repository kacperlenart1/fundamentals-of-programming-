### PLIK 2.3.py: Kompletny program liczący wydatki miesięczne według kategorii, tygodni oraz sumę całkowitą.
monthly_expenses = [  # Wydatki tygodniowe dla kategorii [Food, Transport, Utilities].
    [200, 50, 100],  # Tydzień 1.
    [180, 60, 110],  # Tydzień 2.
    [220, 55, 105],  # Tydzień 3.
    [210, 65, 95]    # Tydzień 4.
]  # Koniec listy wydatków.

food_total = 0  # Suma wydatków na jedzenie.
transport_total = 0  # Suma wydatków na transport.
utilities_total = 0  # Suma wydatków na rachunki.
week_totals = []  # Lista sum wydatków dla każdego tygodnia.

for week in monthly_expenses:  # Przechodzimy przez każdy tydzień w pętli.
    food_total += week[0]  # Dodajemy wydatek na jedzenie z danego tygodnia.
    transport_total += week[1]  # Dodajemy wydatek na transport z danego tygodnia.
    utilities_total += week[2]  # Dodajemy wydatek na rachunki z danego tygodnia.
    week_totals.append(week[0] + week[1] + week[2])  # Zapisujemy łączny wydatek z danego tygodnia.

month_total = food_total + transport_total + utilities_total  # Obliczamy łączny koszt za cały miesiąc.

print("MONTHLY EXPENSES")  # Nagłówek.
print("----------------")  # Linia oddzielająca.
print("Food:", food_total)  # Suma dla kategorii Food.
print("Transport:", transport_total)  # Suma dla kategorii Transport.
print("Utilities:", utilities_total)  # Suma dla kategorii Utilities.
print("Week 1:", week_totals[0])  # Suma dla tygodnia 1.
print("Week 2:", week_totals[1])  # Suma dla tygodnia 2.
print("Week 3:", week_totals[2])  # Suma dla tygodnia 3.
print("Week 4:", week_totals[3])  # Suma dla tygodnia 4.
print("---------------")  # Linia oddzielająca.
print("TOTAL:", month_total)  # Łączna suma wydatków w miesiącu.
