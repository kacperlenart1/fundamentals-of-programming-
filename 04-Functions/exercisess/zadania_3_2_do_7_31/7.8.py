### PLIK 7.8.py: Funkcja wyznaczająca minimalną liczbę monet o nominałach 5, 2 i 1 PLN do wydania kwoty.
def f(amount_to_pay):  # Przyjmujemy kwotę do zapłaty w złotych.
    coins = 0  # Licznik użytych monet.
    for coin in (5, 2, 1):  # Zaczynamy od największego nominału, aby użyć jak najmniej monet.
        coins += amount_to_pay // coin  # Dodajemy tyle monet danego nominału, ile mieści się w pozostałej kwocie.
        amount_to_pay %= coin  # Aktualizujemy resztę kwoty pozostałą do wydania.
    return coins  # Zwracamy minimalną liczbę monet.


print(f(23))  # 4 monety po 5 zł + 1 moneta po 2 zł + 1 moneta po 1 zł = 6 monet.
print(f(8))  # 1 moneta po 5 zł + 1 moneta po 2 zł + 1 moneta po 1 zł = 3 monety.
print(f(2))  # 1 moneta po 2 zł = 1 moneta.
print(f(0))  # Dla kwoty 0 potrzeba 0 monet.
