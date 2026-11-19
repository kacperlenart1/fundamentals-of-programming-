### PLIK 7.4.py: Program sprawdzający liczbę wystąpień litery 'e' w podanym zdaniu.
from letter_counter import count_letter  # Importujemy funkcję count_letter z własnego modułu.

phrase = "You never get a second chance to make a first impression"  # Przykładowe zdanie do analizy.
print(phrase)  # Wypisujemy badane zdanie.
print(f"The number of letter 'e': {count_letter(phrase, 'e')}")  # Wypisujemy liczbę wystąpień litery e.
