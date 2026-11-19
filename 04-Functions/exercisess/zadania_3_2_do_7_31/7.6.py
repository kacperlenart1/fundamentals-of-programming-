### PLIK 7.6.py: Program maskujący numer karty kredytowej z użyciem modułu credit_card.
from credit_card import hide  # Importujemy funkcję maskującą numer karty.

card = "5290312400019022"  # Przykładowy 16-cyfrowy numer karty.
print(hide(card))  # Wypisujemy zamaskowany numer karty.
