### PLIK 3.18.py: Kompletny program testujący wszystkie funkcje modułu MyArrays dla ciągu liczb 7, 3, 8, 5, 2.
import MyArrays  # Importujemy moduł MyArrays z tego samego folderu.

numbers = [7, 3, 8, 5, 2]  # Tablica liczb podana w treści zadania.
extremes = MyArrays.min_max(numbers)  # Pobieramy dwuelementową tablicę [najmniejsza, największa].

print("Numbers:", ",".join(str(x) for x in numbers))  # Wypisujemy ciąg liczb oddzielony przecinkami.
print("Second largest number:", MyArrays.second_largest(numbers))  # Wypisujemy drugą największą liczbę.
print("Difference between largest and smallest:", MyArrays.diff_min_max(numbers))  # Wypisujemy różnicę między maksimum i minimum.
print("Median:", MyArrays.median(numbers))  # Wypisujemy medianę ciągu.
print(f"Smallest and largest number: {extremes[0]},{extremes[1]}")  # Wypisujemy najmniejszą i największą liczbę.
print("Numbers as a string:", MyArrays.to_minus_string(numbers))  # Wypisujemy liczby połączone znakiem minusa.
