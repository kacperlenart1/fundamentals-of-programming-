### PLIK 7.18.py: Funkcja usuwająca wszystkie spacje z podanego zdania.
def f(sentence):  # Przyjmujemy zdanie jako napis.
    return sentence.replace(" ", "")  # Zamieniamy każdą spację na pusty ciąg znaków.


print(f("integrated development environment"))  # Wypisze zdanie bez spacji.
print(f("A programming language is a system of notation for writing computer programs"))  # Wypisze drugie zdanie bez spacji.
