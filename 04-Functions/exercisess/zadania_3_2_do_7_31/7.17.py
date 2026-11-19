### PLIK 7.17.py: Funkcja sprawdzająca czy podany napis czyta się tak samo od początku i od końca.
def f(palindrome):  # Przyjmujemy napis do sprawdzenia.
    return palindrome == palindrome[::-1]  # Porównujemy oryginalny napis z jego odwróconą wersją [::-1].


print(f("radar"))  # Zwróci True.
print(f("12-11-21"))  # Zwróci True.
print(f("book"))  # Zwróci False.
