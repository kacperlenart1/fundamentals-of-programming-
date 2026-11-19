### PLIK 7.16.py: Funkcja zwracająca n-ty wyraz ciągu Fibonacciego liczonego od zera i jedynki.
def f(n):  # Przyjmujemy numer wyrazu ciągu Fibonacciego.
    if n <= 1:  # Pierwszy wyraz to 0, a drugi wyraz to 1.
        return 0 if n == 1 else 0  # Zwracamy wartość początkową dla małych n.
    a, b = 0, 1  # Inicjujemy pierwsze dwa wyrazy ciągu: a = F(1), b = F(2).
    for _ in range(3, n + 1):  # Obliczamy kolejne wyrazy począwszy od trzeciego aż do n.
        a, b = b, a + b  # Przesuwamy wartości: nowy wyraz to suma dwóch poprzednich.
    return b  # Zwracamy n-ty wyraz ciągu.


print(f(5))  # 5. wyraz ciągu Fibonacciego wynosi 3.
print(f(9))  # 9. wyraz ciągu Fibonacciego wynosi 21.
