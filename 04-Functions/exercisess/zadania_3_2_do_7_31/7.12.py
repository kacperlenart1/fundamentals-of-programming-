### PLIK 7.12.py: Funkcja zwracająca n gwiazdek rozdzielonych znakiem ukośnika.
def f(n):  # Przyjmujemy liczbę gwiazdek n.
    if n <= 0:  # Dla zera lub liczby ujemnej zwracamy pusty napis.
        return ""  # Zwracamy pusty string.
    return "/".join(["*"] * n)  # Tworzymy listę n gwiazdek i łączymy je znakiem /.


print(f(4))  # Zwróci "*/*/*/*".
print(f(1))  # Zwróci "*".
