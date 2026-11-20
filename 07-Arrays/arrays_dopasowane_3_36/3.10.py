### PLIK 3.10.py: Kompletny program rysujący wartości [2, 6, 4, 9, 7] jako gwiazdki z użyciem funkcji star(n).
def star(n):  # Zwraca ciąg n gwiazdek jako napis.
    return "*" * n  # Tworzymy napis złożony z n znaków '*'.


arr = [2, 6, 4, 9, 7]  # Tablica liczb całkowitych.
for value in arr:  # Dla każdej liczby w tablicy rysujemy odpowiednią liczbę gwiazdek.
    print(f"{value}: {star(value)}")  # Wypisujemy liczbę, dwukropek oraz gwiazdki.
