### PLIK 7.13.py: Funkcja sklejająca kolejne liczby całkowite od 1 do n w jeden ciąg znaków.
def f(n):  # Przyjmujemy górną granicę n.
    result = ""  # Pusty napis, do którego będziemy doklejać kolejne liczby.
    for i in range(1, n + 1):  # Iterujemy od 1 do n włącznie.
        result += str(i)  # Zamieniamy liczbę i na tekst i dopisujemy na koniec wyniku.
    return result  # Zwracamy połączony ciąg znaków.


print(f(11))  # Zwróci "1234567891011".
print(f(4))  # Zwróci "1234".
