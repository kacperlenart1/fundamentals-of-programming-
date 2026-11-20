### PLIK 1.4.py: Kompletny program wypisujący wszystkie wymagane elementy listy, statystyki oraz wartości rozdzielone spacją.
arr = [2, 3, 7, 5, 4]  # Tworzymy listę z wartościami 2, 3, 7, 5, 4.

print("Array:", arr)  # Wypisujemy całą tablicę.
print("Number of elements:", len(arr))  # Wypisujemy liczbę elementów.
print("First value:", arr[0])  # Wypisujemy pierwszą wartość.
print("Second value:", arr[1])  # Wypisujemy drugą wartość.
print("Last value:", arr[len(arr) - 1])  # Wypisujemy ostatnią wartość bez ujemnego indeksu.
print("Last but one value:", arr[len(arr) - 2])  # Wypisujemy przedostatnią wartość bez ujemnego indeksu.
print("Sum of first and last:", arr[0] + arr[len(arr) - 1])  # Wypisujemy sumę pierwszej i ostatniej wartości.
print("Middle value:", arr[len(arr) // 2])  # Wypisujemy środkową wartość.

print("All values:", end=" ")  # Nagłówek przed wypisaniem wszystkich wartości.
for item in arr:  # Przechodzimy przez każdy element tablicy w pętli.
    print(item, end=" ")  # Wypisujemy element oddzielony pojedynczą spacją.
print()  # Przechodzimy do nowej linii po zakończeniu pętli.
