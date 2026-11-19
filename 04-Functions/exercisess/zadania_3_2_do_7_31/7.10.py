### PLIK 7.10.py: Funkcja zliczająca ujemne liczby parzyste należące do przedziału domkniętego od x do y.
def f(x, y):  # Przyjmujemy początek i koniec przedziału domkniętego.
    count = 0  # Licznik spełniających warunek liczb.
    for num in range(x, y + 1):  # Używamy y + 1, aby uwzględnić prawy koniec przedziału.
        if num < 0 and num % 2 == 0:  # Sprawdzamy czy liczba jest ujemna oraz podzielna przez 2.
            count += 1  # Zwiększamy licznik o 1.
    return count  # Zwracamy liczbę znalezionych liczb.


print(f(-7, 8))  # Ujemne parzyste w tym przedziale to -6, -4 i -2, czyli 3 liczby.
print(f(-1, 11))  # Brak ujemnych liczb parzystych, wynik to 0.
