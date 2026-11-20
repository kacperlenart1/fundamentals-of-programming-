### PLIK 3.11.py: Kompletna funkcja compare(array1, array2) oraz porównanie wszystkich 4 par tablic z zadania.
def compare(array1, array2):  # Zwraca True, gdy obie tablice mają tę samą długość i równe elementy na tych samych indeksach.
    if len(array1) != len(array2):  # Jeśli długości różnią się, tablice nie są takie same.
        return False  # Zwracamy False.
    for i in range(len(array1)):  # Sprawdzamy każdy indeks po kolei.
        if array1[i] != array2[i]:  # Jeśli elementy na tym samym indeksie różnią się.
            return False  # Zwracamy False.
    return True  # Wszystkie elementy i długości są zgodne.


test_pairs = [  # Cztery pary tablic z polecenia zadania.
    (["water", "book", "sky"], ["water", "book", "sky"]),  # Para 1.
    ([True, False], [True, False, True]),  # Para 2.
    ([5, 3, 1], [5, 3, 1]),  # Para 3.
    ([3, 2, 1], [3, 2]),  # Para 4.
]  # Koniec listy par.

for array1, array2 in test_pairs:  # Dla każdej pary wypisujemy obie tablice i wynik porównania.
    print("Array1:", *array1)  # Wypisujemy pierwszą tablicę.
    print("Array2:", *array2)  # Wypisujemy drugą tablicę.
    result_text = "arrays are the same" if compare(array1, array2) else "arrays are not the same"  # Opis wyniku.
    print("Comparison:", result_text)  # Wypisujemy wynik porównania.
    print()  # Wypisujemy pustą linię pomiędzy wynikami.
