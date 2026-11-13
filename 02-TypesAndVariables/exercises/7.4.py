###
# Program sprawdzający, czy drzewo może zostać ścięte
# na podstawie jego obwodu (średnica musi wynosić co najmniej 50 cm).
#

import math

# Pobranie obwodu drzewa od użytkownika i konwersja na liczbę zmiennoprzecinkową
circumference = float(input('Enter tree circumference in cm: '))

# Obliczenie średnicy drzewa (średnica = obwód / pi)
diameter = circumference / math.pi

# Sprawdzenie warunku: czy średnica wynosi co najmniej 50 cm
can_be_cut = diameter >= 50

# Wyświetlenie wyniku (True / False)
print(f'Tree can be cut down: {can_be_cut}')