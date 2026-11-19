### PLIK months.py: Moduł zwracający angielską nazwę miesiąca na podstawie jego numeru od 1 do 12.
def month(n):  # Definiujemy funkcję przyjmującą numer miesiąca n.
    names = [  # Tworzymy listę nazw miesięcy w kolejności od stycznia do grudnia.
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]  # Koniec listy nazw miesięcy.
    if 1 <= n <= 12:  # Sprawdzamy czy numer miesiąca mieści się w poprawnym zakresie od 1 do 12.
        return names[n - 1]  # Odejmij 1, ponieważ indeksy list w Pythonie zaczynają się od zera.
    return ""  # Zwracamy pusty napis dla niepoprawnego numeru miesiąca.
