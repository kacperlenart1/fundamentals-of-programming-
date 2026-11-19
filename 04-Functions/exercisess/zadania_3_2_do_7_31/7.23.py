### PLIK 7.23.py: Funkcja sprawdzająca czy hasło ma co najmniej 6 znaków i każdy znak występuje tylko raz.
def f(password):  # Przyjmujemy hasło jako napis.
    if len(password) < 6:  # Hasło krótsze niż 6 znaków jest od razu odrzucane.
        return False  # Zwracamy False dla zbyt krótkiego hasła.
    return len(set(password)) == len(password)  # Zbiór set usuwa duplikaty; gdy długości są równe, znaki się nie powtarzają.


print(f("ax15"))  # Za krótkie hasło, zwróci False.
print(f("book123"))  # Litera o występuje dwa razy, zwróci False.
print(f("A2water3"))  # Ma 8 znaków i wszystkie są unikalne, zwróci True.
print(f("qwerty"))  # Ma 6 unikalnych znaków, zwróci True.
print(f(""))  # Puste hasło, zwróci False.
