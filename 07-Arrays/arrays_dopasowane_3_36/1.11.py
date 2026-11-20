### PLIK 1.11.py: Kompletny program analizujący temperatury z marca i wypisujący pełny raport pogodowy.
temperatures = [  # Dzienne pomiary temperatury z marca.
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]  # Koniec listy temperatur.

measurements = len(temperatures)  # Obliczamy liczbę pomiarów.

temp_total = 0  # Zmienna przechowująca sumę temperatur.
for temp in temperatures:  # Sumujemy wszystkie pomiary w pętli for.
    temp_total += temp  # Dodajemy bieżący pomiar do sumy.
avg_temp = temp_total / measurements  # Obliczamy średnią temperaturę w miesiącu.

min_temp = min(temperatures)  # Wyznaczamy minimalną temperaturę.
max_temp = max(temperatures)  # Wyznaczamy maksymalną temperaturę.

negative_temp = 0  # Licznik dni z ujemną temperaturą.
i = 0  # Indeks początkowy dla pętli while.
while i < measurements:  # Przeglądamy wszystkie pomiary w pętli while.
    if temperatures[i] < 0:  # Sprawdzamy czy temperatura danego dnia była ujemna.
        negative_temp += 1  # Zwiększamy licznik dni z ujemną temperaturą.
    i += 1  # Przechodzimy do kolejnego dnia.

print("TEMPERATURE REPORT")  # Nagłówek raportu.
print("Month: March")  # Nazwa miesiąca.
print("Number of measurements:", measurements)  # Liczba pomiarów.
print(f"Average temperature in the month: {avg_temp:.2f}")  # Średnia temperatura.
print("Minimum temperature:", min_temp)  # Minimalna temperatura.
print("Maximum temperature:", max_temp)  # Maksymalna temperatura.
print("Number of days with negative temperature:", negative_temp)  # Liczba dni z ujemną temperaturą.
