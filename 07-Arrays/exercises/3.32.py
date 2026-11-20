### PLIK 3.32.py: Kompletny program zamieniający pierwszy i ostatni wiersz tablicy 3 na 5 przed i po zmianie.
arr = [  # Tablica dwuwymiarowa o rozmiarze 3 na 5.
    [1, 2, 3, 4, 5],  # Pierwszy wiersz.
    [6, 7, 8, 9, 10],  # Środkowy wiersz.
    [11, 12, 13, 14, 15]  # Ostatni wiersz.
]  # Koniec tablicy.

print("Before swap:")  # Nagłówek przed zamianą wierszy.
for row in arr:  # Wypisujemy tablicę przed zmianą w wierszach i kolumnach.
    print(*row)  # Wypisujemy wartości wiersza.

arr[0], arr[-1] = arr[-1], arr[0]  # Zamieniamy pierwszy wiersz z ostatnim wierszem.

print("After swap:")  # Nagłówek po zamianie wierszy.
for row in arr:  # Wypisujemy tablicę po zmianie w wierszach i kolumnach.
    print(*row)  # Wypisujemy wartości wiersza.
