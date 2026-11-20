### PLIK 3.4.py: Kompletny program wypisujący tablicę [15, 8, 31, 47, 2, 19] w kolejności oryginalnej oraz odwrotnej w pętli.
arr = [15, 8, 31, 47, 2, 19]  # Tablica liczb naturalnych.

print("existed array:", end=" ")  # Wypisujemy początek linii dla oryginalnej tablicy.
for value in arr:  # Przechodzimy po elementach w oryginalnej kolejności.
    print(value, end=" ")  # Wypisujemy element i spację.
print()  # Przechodzimy do nowej linii.

print("reverse array:", end=" ")  # Wypisujemy początek linii dla odwróconej tablicy.
for i in range(len(arr) - 1, -1, -1):  # Przechodzimy od ostatniego indeksu do pierwszego.
    print(arr[i], end=" ")  # Wypisujemy element i spację.
print()  # Przechodzimy do nowej linii.
