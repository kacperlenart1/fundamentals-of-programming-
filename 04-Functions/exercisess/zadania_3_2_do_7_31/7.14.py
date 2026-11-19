### PLIK 7.14.py: Funkcja wykonująca wskazane działanie arytmetyczne na dwóch liczbach.
def f(number1, number2, operator):  # Przyjmujemy dwie liczby oraz znak operatora.
    if operator == "+":  # Dodawanie.
        return number1 + number2  # Zwracamy sumę.
    elif operator == "-":  # Odejmowanie.
        return number1 - number2  # Zwracamy różnicę.
    elif operator == "*":  # Mnożenie.
        return number1 * number2  # Zwracamy iloczyn.
    elif operator == "%":  # Reszta z dzielenia (modulo).
        return number1 % number2  # Zwracamy resztę z dzielenia.
    elif operator == "**":  # Potęgowanie.
        return number1 ** number2  # Zwracamy wynik potęgowania.
    return None  # Zwracamy None, gdy operator jest inny niż dozwolone.


print(f(2, 3, "+"))  # Wynik: 5.
print(f(2, 3, "%"))  # Wynik: 2.
print(f(2, 3, "**"))  # Wynik: 8.
print(f(2, 3, "*"))  # Wynik: 6.
print(f(2, 3, "-"))  # Wynik: -1.
