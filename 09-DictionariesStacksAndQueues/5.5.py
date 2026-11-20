### PLIK 5.5.py: Program zliczający ile razy każde słowo występuje w podanym akapicie.
paragraph = "cat dog mouse cat rat cat mouse"  # Tekst wejściowy.
word_counts = {}  # Pusty słownik na liczniki słów.

for word in paragraph.split():  # Dzielimy tekst na słowa i iterujemy po nich.
    if word in word_counts:  # Jeśli słowo jest już w słowniku.
        word_counts[word] += 1  # Zwiększamy jego licznik o 1.
    else:  # Jeśli słowo pojawia się po raz pierwszy.
        word_counts[word] = 1  # Ustawiamy początkowy licznik na 1.

for word, count in word_counts.items():  # Wypisujemy każde słowo i liczbę jego wystąpień.
    print(f"{word}: {count}")  # Wyświetlamy wynik.
