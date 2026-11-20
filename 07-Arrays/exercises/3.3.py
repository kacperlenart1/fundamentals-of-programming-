### PLIK 3.3.py: Kompletny program zliczający liczby parzyste w tablicy [34, 7, 19, 4, 21, 8] z użyciem pętli while.
arr = [34, 7, 19, 4, 21, 8]  # Tablica liczb całkowitych.
even_count = 0  # Licznik liczb parzystych.
i = 0  # Indeks początkowy dla pętli while.

while i < len(arr):  # Przechodzimy przez wszystkie elementy tablicy w pętli while.
    if arr[i] % 2 == 0:  # Sprawdzamy czy bieżący element jest parzysty.
        even_count += 1  # Zwiększamy licznik liczb parzystych.
    i += 1  # Przechodzimy do następnego indeksu.

print("Array:", arr)  # Wypisujemy zawartość tablicy.
print("Number of even values:", even_count)  # Wypisujemy liczbę wartości parzystych.
