### PLIK 3.28.py: Kompletny program obliczający sumę wartości w ostatniej kolumnie tablicy dwuwymiarowej.
arr = [  # Tablica dwuwymiarowa z zadania.
    [7, 3, 7, 9, 0],  # Wiersz 1.
    [2, 9, 0, 1, 5],  # Wiersz 2.
    [3, 8, 6, 4, 7],  # Wiersz 3.
    [8, 7, 1, 1, 5]   # Wiersz 4.
]  # Koniec tablicy.

last_col_sum = 0  # Zmienna przechowująca sumę ostatniej kolumny.
for row in arr:  # Przechodzimy przez każdy wiersz tablicy.
    last_col_sum += row[-1]  # Dodajemy ostatni element bieżącego wiersza.

print("Sum of values in the last column:", last_col_sum)  # Wypisujemy sumę ostatniej kolumny.
