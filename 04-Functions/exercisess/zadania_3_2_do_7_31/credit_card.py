### PLIK credit_card.py: Moduł maskujący numer karty tak aby widoczne były tylko pierwsze dwie i ostatnie cztery cyfry.
def hide(card_number):  # Przyjmujemy numer karty jako napis lub liczbę.
    s = str(card_number)  # Zamieniamy numer karty na ciąg znaków.
    if len(s) < 6:  # Zabezpieczamy się na wypadek zbyt krótkiego napisu.
        return s  # Zwracamy napis bez zmian, jeśli ma mniej niż 6 znaków.
    return s[:2] + "*" * (len(s) - 6) + s[-4:]  # Łączymy pierwsze 2 znaki, gwiazdki w środku oraz ostatnie 4 znaki.
