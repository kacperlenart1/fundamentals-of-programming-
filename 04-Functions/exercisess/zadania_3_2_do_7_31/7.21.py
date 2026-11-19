### PLIK 7.21.py: Funkcja zwracająca różnicę pomiędzy największą a najmniejszą spośród trzech liczb.
def f(number1, number2, number3):  # Przyjmujemy trzy liczby.
    return max(number1, number2, number3) - min(number1, number2, number3)  # Odejmujemy minimum od maksimum.


print(f(7, 4, 9))  # Największa 9, najmniejsza 4, różnica wynosi 5.
print(f(2, 12, 8))  # Największa 12, najmniejsza 2, różnica wynosi 10.
