### PLIK 3.30.py: Kompletny program modyfikujący tablicę 5x5 w pętlach w tabliczkę mnożenia (1..5) i wypisujący wynik.
arr = [[0 for _ in range(5)] for _ in range(5)]  # Tablica 5x5 wypełniona zerami.

for i in range(5):  # Przechodzimy po numerach wierszy (0..4).
    for j in range(5):  # Przechodzimy po numerach kolumn (0..4).
        arr[i][j] = (i + 1) * (j + 1)  # Wpisujemy iloczyn numeru wiersza i kolumny (od 1 do 5).

for row in arr:  # Wypisujemy tabliczkę mnożenia w wierszach i kolumnach.
    for val in row:  # Wypisujemy każdą wartość z wiersza.
        print(f"{val:2d}", end=" ")  # Wyrównujemy liczbę na 2 znakach.
    print()  # Przechodzimy do nowej linii po każdym wierszu.
