### PLIK 7.11.py: Funkcja zwracająca True jeśli przynajmniej jedna z podanych trzech liczb jest ujemna.
def f(n1, n2, n3):  # Przyjmujemy trzy liczby.
    return n1 < 0 or n2 < 0 or n3 < 0  # Operator or daje True, jeśli choć jeden z warunków jest prawdziwy.


print(f(11, 6, -4))  # Zwróci True, ponieważ -4 jest ujemne.
print(f(5, 4, 14))  # Zwróci False, bo wszystkie liczby są dodatnie.
