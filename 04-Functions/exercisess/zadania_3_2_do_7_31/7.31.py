### PLIK 7.31.py: Funkcja rekurencyjna obliczająca potęgę liczby x do potęgi n oraz jej wynik dla 5 do potęgi 3.
def power(x, n):  # Funkcja licząca x podniesione do potęgi n.
    if n == 0:  # Warunek bazowy: każda liczba podniesiona do potęgi 0 daje 1.
        return 1  # Zwracamy 1.
    return x * power(x, n - 1)  # Korzystamy z zależności x^n = x * x^(n-1).


print(power(5, 3))  # 5 do potęgi 3 wynosi 125.
