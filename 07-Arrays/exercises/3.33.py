### PLIK 3.33.py: Kompletny program zamieniający pierwszą i ostatnią kolumnę tablicy 3 na 5 przed i po zmianie.
arr = [  # Tablica dwuwymiarowa o rozmiarze 3 na 5.
    [1, 2, 3, 4, 5],  # Pierwszy wiersz.
    [6, 7, 8, 9, 10],  # Środkowy wiersz.
    [11, 12, 13, 14, 15]  # Ostatni wiersz.
]  # Koniec tablicy.

print("Before swap:")  # Nagłówek przed zamianą kolumn.
for row in arr:  # Wypisujemy tablicę przed zmianą w wierszach i kolumnach.
    print(*row)  # Wypisujemy wartości wiersza.

for row in arr:  # W każdym wierszu zamieniamy pierwszy element z ostatnim.
    row[0], row[-1] = row[-1], row[0]  # Zamiana pierwszej i ostatniej kolumny.

print("After swap:")  # Nagłówek po zamianie kolumn.
for row in arr:  # Wypisujemy tablicę po zmianie w wierszach i kolumnach.
    print(*row)  # Wypisujemy wartości wiersza.
