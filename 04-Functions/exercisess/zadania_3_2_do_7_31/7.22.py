### PLIK 7.22.py: Funkcja tworząca akronim z pierwszych liter każdego słowa w podanym tekście.
def f(name):  # Przyjmujemy tekst składający się ze słów.
    words = name.split()  # Dzielimy tekst na listę pojedynczych słów względem spacji.
    return "".join(word[0] for word in words if word)  # Bierzemy pierwszy znak każdego słowa i łączymy w jeden napis.


print(f("Internet of Things"))  # Zwróci "IoT".
print(f("For Your Information"))  # Zwróci "FYI".
print(f("Python"))  # Zwróci "P".
