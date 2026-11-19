### PLIK 7.19.py: Funkcja obliczająca sumę wszystkich wystąpień cyfr które pojawiają się w liczbie więcej niż raz.
def f(number):  # Przyjmujemy liczbę całkowitą.
    s = str(abs(number))  # Zamieniamy wartość bezwzględną liczby na tekst.
    total = 0  # Zmienna sumująca powtarzające się cyfry.
    for ch in s:  # Przechodzimy po każdym znaku w liczbie.
        if s.count(ch) > 1:  # Sprawdzamy czy dana cyfra występuje w napisie więcej niż jeden raz.
            total += int(ch)  # Dodajemy wartość cyfry do sumy.
    return total  # Zwracamy końcową sumę.


print(f(1027))  # Żadna cyfra się nie powtarza, wynik to 0.
print(f(230335))  # Powtarza się cyfra 3 (trzy razy), suma wynosi 3 + 3 + 3 = 9.
print(f(513553007))  # Powtarzają się 5, 3 oraz 0, suma wynosi 21.
