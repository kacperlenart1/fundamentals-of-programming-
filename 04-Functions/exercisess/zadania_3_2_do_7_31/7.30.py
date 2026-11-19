### PLIK 7.30.py: Funkcja rekurencyjna obliczająca sumę liczb naturalnych od 1 do n oraz jej wywołanie dla n równego 10.
def sum_natural(n):  # Funkcja sumująca liczby od 1 do n za pomocą rekurencji.
    if n <= 1:  # Warunek bazowy dla najmniejszej liczby naturalnej równej 1.
        return n  # Zwracamy n i przerywamy rekurencję.
    return n + sum_natural(n - 1)  # Dodajemy n do sumy wszystkich liczb od 1 do n - 1.


print(sum_natural(10))  # Suma liczb od 1 do 10 wynosi 55.
