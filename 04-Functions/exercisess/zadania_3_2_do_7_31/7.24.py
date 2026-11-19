### PLIK 7.24.py: Funkcja obliczająca wartość wyrażenia składającego się z jednocyfrowych liczb oraz znaków plus i minus.
def f(expression):  # Przyjmujemy napis z działaniem dodawania i odejmowania.
    total = 0  # Bieżący wynik działania.
    sign = 1  # Aktualny znak działania: 1 oznacza dodawanie, a -1 oznacza odejmowanie.
    for ch in expression:  # Przechodzimy po każdym znaku wyrażenia.
        if ch == "+":  # Trafiamy na znak plus.
            sign = 1  # Ustawiamy znak na dodatni.
        elif ch == "-":  # Trafiamy na znak minus.
            sign = -1  # Ustawiamy znak na ujemny.
        elif ch.isdigit():  # Jeśli znak jest cyfrą.
            total += sign * int(ch)  # Dodajemy lub odejmujemy cyfrę w zależności od aktualnego znaku.
    return total  # Zwracamy obliczoną wartość wyrażenia.


print(f("2+3"))  # Wynik: 5.
print(f("3+8+1"))  # Wynik: 12.
print(f("2+3-4+5-0"))  # Wynik: 6.
