### PLIK 7.20.py: Funkcja wyznaczająca n-tą liczbę pierwszą zaczynając od 2.
def f(n):  # Przyjmujemy numer szukanej liczby pierwszej n.
    count = 0  # Licznik znalezionych liczb pierwszych.
    candidate = 2  # Pierwsza liczba pierwsza to 2, od niej zaczynamy sprawdzanie.
    while True:  # Pętla działa dopóki nie znajdziemy n-tej liczby pierwszej.
        is_prime = True  # Zakładamy na start, że kandydat jest liczbą pierwszą.
        for d in range(2, int(candidate ** 0.5) + 1):  # Sprawdzamy dzielniki tylko do pierwiastka z kandydata.
            if candidate % d == 0:  # Jeśli reszta z dzielenia wynosi 0, liczba ma dzielnik i nie jest pierwsza.
                is_prime = False  # Oznaczamy kandydata jako złożonego.
                break  # Przerywamy pętlę sprawdzającą dzielniki.
        if is_prime:  # Jeśli kandydat okazał się liczbą pierwszą.
            count += 1  # Zwiększamy licznik liczb pierwszych.
            if count == n:  # Sprawdzamy czy to już szukana n-ta liczba pierwsza.
                return candidate  # Zwracamy znalezioną liczbę pierwszą.
        candidate += 1  # Przechodzimy do kolejnej liczby całkowitej.


print(f(1))  # Pierwsza liczba pierwsza to 2.
print(f(5))  # Piąta liczba pierwsza to 11.
