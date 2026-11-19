### PLIK range_checker.py: Moduł z funkcją sprawdzającą czy liczba należy do domkniętego przedziału od x do y.
def in_range(number, x, y):  # Przyjmujemy badaną liczbę oraz granice przedziału x i y.
    return x <= number <= y  # Zwracamy True gdy liczba jest między x a y włącznie, w przeciwnym razie False.
