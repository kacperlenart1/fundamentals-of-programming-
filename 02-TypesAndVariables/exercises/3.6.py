###
# Program obliczający odległość do horyzontu
# w zależności od wysokości obserwatora (w metrach).
#
import math

# Pobranie wysokości od użytkownika z klawiatury
height = float(input("Podaj wysokość obserwatora w metrach: "))

# Obliczenie odległości do horyzontu w kilometrach
distance = 3.57 * math.sqrt(height)

# Wydrukowanie wyniku
print("Przy wysokości", height, "m, odległość do horyzontu wynosi:", round(distance, 2), "km")