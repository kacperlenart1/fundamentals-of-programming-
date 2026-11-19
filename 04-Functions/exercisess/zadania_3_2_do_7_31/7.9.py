### PLIK 7.9.py: Funkcja zwracająca sumę cyfr parzystych albo nieparzystych w zależności od parametru even.
def f(number, even):  # Przyjmujemy liczbę oraz flagę logiczną even.
    total = 0  # Zmienna przechowująca sumę wybranych cyfr.
    for ch in str(abs(number)):  # Przechodzimy po każdej cyfrze liczby bez znaku minus.
        digit = int(ch)  # Zamieniamy znak na liczbę całkowitą.
        if even and digit % 2 == 0:  # Gdy even jest True, sumujemy tylko cyfry parzyste.
            total += digit  # Dodajemy cyfrę parzystą do sumy.
        elif not even and digit % 2 != 0:  # Gdy even jest False, sumujemy tylko cyfry nieparzyste.
            total += digit  # Dodajemy cyfrę nieparzystą do sumy.
    return total  # Zwracamy obliczoną sumę cyfr.


print(f(3124, True))  # Cyfry parzyste to 2 i 4, suma wynosi 6.
print(f(3124, False))  # Cyfry nieparzyste to 3 i 1, suma wynosi 4.
print(f(20576, False))  # Cyfry nieparzyste to 5 i 7, suma wynosi 12.
print(f(20576, True))  # Cyfry parzyste to 2, 0 i 6, suma wynosi 8.
print(f(13115, True))  # Brak cyfr parzystych, więc suma wynosi 0.
