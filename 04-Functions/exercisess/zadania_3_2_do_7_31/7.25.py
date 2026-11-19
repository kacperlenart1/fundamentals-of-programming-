### PLIK 7.25.py: Funkcja sumująca liczby z przedziału domkniętego podzielne przez 2 i 3 oraz niepodzielne przez 4.
def f(x, y):  # Przyjmujemy granice przedziału x oraz y.
    total = 0  # Suma liczb spełniających wszystkie warunki.
    for num in range(x, y + 1):  # Sprawdzamy każdą liczbę całkowitą z przedziału <x, y>.
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:  # Warunek podzielności przez 2 i 3 oraz braku podzielności przez 4.
            total += num  # Dodajemy pasującą liczbę do sumy.
    return total  # Zwracamy sumę.


print(f(1, 20))  # Pasuje tylko 6 i 18, ich suma to 24.
print(f(10, 30))  # Pasuje 18 i 30, ich suma to 48.
