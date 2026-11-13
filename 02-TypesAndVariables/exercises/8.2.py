###
# Program do obliczania pola powierzchni i obwodu koła na podstawie podanego promienia (r).
#

import math

# Pobranie promienia od użytkownika i konwersja na liczbę zmiennoprzecinkową
r = float(input('Enter radius: '))

# Obliczenie pola powierzchni (area = pi * r^2)
area = math.pi * r ** 2

# Obliczenie obwodu (circumference = 2 * pi * r)
circumference = 2 * math.pi * r

# Wyświetlenie wyników z formatowaniem do dwóch miejsc po przecinku
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')