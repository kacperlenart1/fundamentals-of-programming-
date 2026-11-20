### PLIK 3.12.py: Kompletny program wypisujący liczby z pierwszej tablicy, które nie występują w drugiej tablicy.
array1 = [4, 36, 12, 28, 9, 44, 5]  # Pierwsza tablica liczb całkowitych.
array2 = [5, 1, 36]  # Druga tablica liczb całkowitych.

diff_elements = []  # Lista liczb z array1 nieobecnych w array2.
for item in array1:  # Sprawdzamy każdy element pierwszej tablicy.
    if item not in array2:  # Jeśli element nie występuje w drugiej tablicy.
        diff_elements.append(item)  # Dopisujemy go do listy wynikowej.

print("Array1:", *array1)  # Wypisujemy pierwszą tablicę.
print("Array2:", *array2)  # Wypisujemy drugą tablicę.
print("Numbers from array1 not in array2:", *diff_elements)  # Wypisujemy znalezione liczby.
