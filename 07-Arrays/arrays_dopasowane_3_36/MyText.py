### PLIK MyText.py: Kompletny moduł z 3 funkcjami analizującymi tekst: liczba słów, od najdłuższych oraz alfabetycznie.
def word_count(text):  # Funkcja 1: zwraca liczbę słów w tekście.
    return len(text.split())  # Dzielimy tekst po białych znakach i zwracamy liczbę słów.


def words_longest_first(text):  # Funkcja 2: zwraca tablicę słów posortowaną od najdłuższych do najkrótszych.
    words = text.split()  # Pobieramy listę słów z tekstu.
    return sorted(words, key=len, reverse=True)  # Sortujemy po długości słowa malejąco.


def words_alphabetical(text):  # Funkcja 3: zwraca tablicę słów posortowaną alfabetycznie.
    words = text.split()  # Pobieramy listę słów z tekstu.
    return sorted(words)  # Sortujemy słowa alfabetycznie.
