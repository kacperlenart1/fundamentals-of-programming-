### PLIK 3.8.py: Kompletny program obliczający średnią arytmetyczną elementów tablicy [15, 8, 31, 47, 2, 19] w pętli while.
arr = [15, 8, 31, 47, 2, 19]  # Tablica wartości.
total = 0  # Suma elementów tablicy.
i = 0  # Indeks początkowy dla pętli while.

while i < len(arr):  # Przeglądamy wszystkie elementy tablicy w pętli while.
    total += arr[i]  # Dodajemy bieżący element do sumy.
    i += 1  # Przechodzimy do kolejnego elementu.

mean = total / len(arr)  # Obliczamy średnią arytmetyczną.
print("Array:", *arr)  # Wypisujemy elementy tablicy.
print("Arithmetic mean:", mean)  # Wypisujemy średnią arytmetyczną.
