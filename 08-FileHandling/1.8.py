import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 1.8.py: Program wypisujący zawartość pliku pets.txt oraz zliczający łączną liczbę słów w tekście.
with open('pets.txt', 'r', encoding='utf-8') as file:  # Otwieramy plik pets.txt do odczytu.
    total_words = 0  # Licznik wszystkich słów w tekście.
    for line in file:  # Czytamy plik linia po linii.
        print(line, end="")  # Wypisujemy treść bieżącej linii.
        words = line.split()  # Dzielimy linię po białych znakach na listę słów.
        total_words += len(words)  # Dodajemy liczbę słów z tej linii do sumy.

print()  # Przechodzimy do nowej linii po wypisaniu całego tekstu.
print('Number of words:', total_words)  # Wypisujemy łączną liczbę słów w pliku.
