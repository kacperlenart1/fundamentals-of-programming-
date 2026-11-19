### PLIK 7.26.py: Funkcja rozdzielająca wszystkie znaki podanego napisu pojedynczym myślnikiem.
def f(text):  # Przyjmujemy tekst wejściowy.
    return "-".join(text)  # Wstawiamy myślnik pomiędzy każdy kolejny znak w napisie.


print(f("Univesity"))  # Wypisze znaki rozdzielone myślnikiem.
print(f("UE"))  # Wypisze "U-E".
print(f("x"))  # Dla jednego znaku nie ma co rozdzielać, zwróci "x".
print(f(""))  # Dla pustego napisu zwróci "".
