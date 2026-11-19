### PLIK 7.7.py: Funkcja sprawdzająca czy podany napis składa się wyłącznie z cyfr 0 i 1.
def f(binary_number):  # Przyjmujemy napis reprezentujący liczbę binarną.
    if not binary_number:  # Pusty ciąg znaków nie jest poprawną liczbą binarną.
        return False  # Zwracamy False dla pustego napisu.
    for ch in binary_number:  # Sprawdzamy każdy znak po kolei.
        if ch not in ("0", "1"):  # Jeśli znak jest inny niż 0 lub 1.
            return False  # Zwracamy False i przerywamy sprawdzanie.
    return True  # Wszystkie znaki to 0 lub 1, więc zwracamy True.


print(f("101101"))  # Powinno zwrócić True.
print(f("1311a10100"))  # Powinno zwrócić False ze względu na cyfry inne niż 0/1 oraz literę a.
