### PLIK 3.31.py: Program znajdujący najmniejszą i największą wartość w tablicy 2D oraz ich wiersz i kolumnę.
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]  # Tablica liczb całkowitych z zadania.

smallest = arr[0][0]  # Najmniejsza wartość na starcie.
smallest_row = 0  # Indeks wiersza najmniejszej wartości.
smallest_col = 0  # Indeks kolumny najmniejszej wartości.

largest = arr[0][0]  # Największa wartość na starcie.
largest_row = 0  # Indeks wiersza największej wartości.
largest_col = 0  # Indeks kolumny największej wartości.

for r in range(len(arr)):  # Przechodzimy po wierszach tablicy.
    for c in range(len(arr[r])):  # Przechodzimy po kolumnach w bieżącym wierszu.
        value = arr[r][c]  # Pobieramy element tablicy.
        if value < smallest:  # Jeśli element jest mniejszy od dotychczasowego minimum.
            smallest = value  # Aktualizujemy najmniejszą wartość.
            smallest_row = r  # Zapisujemy indeks wiersza.
            smallest_col = c  # Zapisujemy indeks kolumny.
        if value > largest:  # Jeśli element jest większy od dotychczasowego maksimum.
            largest = value  # Aktualizujemy największą wartość.
            largest_row = r  # Zapisujemy indeks wiersza.
            largest_col = c  # Zapisujemy indeks kolumny.

print(f"Smallest value: {smallest} (row: {smallest_row + 1}, column: {smallest_col + 1})")  # Wypisujemy minimum i czytelny numer wiersza oraz kolumny.
print(f"Largest value: {largest} (row: {largest_row + 1}, column: {largest_col + 1})")  # Wypisujemy maksimum i czytelny numer wiersza oraz kolumny.