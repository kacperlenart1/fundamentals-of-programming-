import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.6.py: Program liczący linie, znaki i słowa w podanym pliku tekstowym z obsługą błędu braku pliku.
file_name = input("File name: ")  # Wczytujemy nazwę pliku od użytkownika.

try:  # Próbujemy otworzyć plik i policzyć statystyki.
    with open(file_name, "r", encoding="utf-8") as file:  # Otwieramy plik w kodowaniu UTF-8.
        content = file.read()  # Wczytujemy całą zawartość pliku.
    num_lines = len(content.splitlines())  # Liczymy liczbę linii w pliku.
    num_chars = len(content)  # Liczymy łączną liczbę znaków w pliku.
    num_words = len(content.split())  # Liczymy łączną liczbę słów w pliku.
    print(f"Number of lines: {num_lines}")  # Wypisujemy liczbę linii.
    print(f"Number of characters: {num_chars}")  # Wypisujemy liczbę znaków.
    print(f"Number of words: {num_words}")  # Wypisujemy liczbę słów.
except FileNotFoundError:  # Przechwytujemy błąd, gdy podany plik nie istnieje.
    print(f"File '{file_name}' was not found.")  # Wypisujemy komunikat o braku pliku bez przerywania programu.
