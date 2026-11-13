###
# Program obliczający objętość i pole powierzchni prostopadłościanu
# o bokach a, b i c wczytywanych z klawiatury.
#

# Wczytanie wymiarów prostopadłościanu z klawiatury i konwersja na liczby całkowite
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

# Obliczenie objętości (iloczyn wszystkich boków)
volume = a * b * c

# Obliczenie pola powierzchni całkowitej (suma pól wszystkich ścian)
surface_area = 2 * (a * b + b * c + a * c)

# Wyświetlenie wyników z użyciem f-stringów
print(f'Cuboid dimensions: a = {a}, b = {b}, c = {c}')
print(f'Volume = {volume}')
print(f'Surface area = {surface_area}')