### PLIK 3.27.py: Kompletny program wypisujący tablicę dwuwymiarową 2 na 4 w wierszach i kolumnach.
arr_2x4 = [  # Tablica dwuwymiarowa o rozmiarze 2 wiersze na 4 kolumny.
    [10, 20, 30, 40],  # Pierwszy wiersz.
    [50, 60, 70, 80]   # Drugi wiersz.
]  # Koniec tablicy.

for row in arr_2x4:  # Przechodzimy przez każdy wiersz.
    for col_val in row:  # Przechodzimy przez każdą kolumnę w wierszu.
        print(col_val, end=" ")  # Wypisujemy wartość i spację.
    print()  # Przechodzimy do nowej linii po zakończeniu wiersza.
