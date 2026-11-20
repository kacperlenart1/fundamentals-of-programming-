### PLIK 3.31.py: Kompletny program znajdujący najmniejszą i największą wartość w tablicy 2D oraz ich wiersz i kolumnę.
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]  # Tablica liczb całkowitych z zadania.

smallest = arr[0][0]  # Najmniejsza wartość na starcie.
smallest_row = 0  # Wiersz najmniejszej wartości.
smallest_col = 0  # Kolumna najmniejszej wartości.

largest = arr[0][0]  # Największa wartość na starcie.
largest_row = 0  # Wiersz największej wartości.
largest_col = 0  # Kolumna największej wartości.

for r in range(len(arr)):  # Przechodzimy po wierszach tablicy.
    for c in range(len(arr[r])):  # Przechodzimy po kolumnach w bieżącym wierszu.
        value = arr[r][c]  # Pobieramy element tablicy.
        if value < smallest:  # Jeśli element jest mniejszy od dotychczasowego minimum.
            smallest = value  # Aktualizujemy najmniejszą wartość.
            smallest_row = r  # Zapisujemy numer wiersza.
            smallest_col = c  # Zapisujemy numer kolumny.
        if value > largest:  # Jeśli element jest większy od dotychczasowego maksimum.
            largest = value  # Aktualizujemy największą wartość.
            largest_row = r  # Zapisujemy numer wiersza.
            largest_col = c  # Zapisujemy numer kolumny.

print(f"Smallest value: {smallest} (row: {smallest_row}, column: {smallest_col})")  # Wypisujemy minimum i pozycję.
print(f"Largest value: {largest} (row: {largest_row}, column: {largest_col})")  # Wypisujemy maksimum i pozycję.
