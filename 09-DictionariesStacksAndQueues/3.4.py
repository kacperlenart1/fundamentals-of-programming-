### PLIK 3.4.py: Program zamieniający liczbę naturalną na system binarny z wykorzystaniem stosu LIFO.
import queue  # Importujemy moduł queue.

number = int(input("Enter natural number: "))  # Wczytujemy liczbę naturalną od użytkownika.
stack = queue.LifoQueue()  # Stos na reszty z dzielenia przez 2.

current = number  # Kopia liczby do dzielenia przez 2.
if current == 0:  # Przypadek szczególny dla liczby 0.
    stack.put(0)  # Wrzucamy 0 na stos.
else:  # Dla liczb dodatnich dzielimy przez 2 aż do uzyskania 0.
    while current > 0:  # Powtarzamy dopóki dzielona liczba jest większa od 0.
        remainder = current % 2  # Wyznaczamy resztę z dzielenia przez 2.
        stack.put(remainder)  # Odkładamy resztę na stos.
        current //= 2  # Dzielimy całkowicie przez 2.

binary_digits = []  # Lista przechowująca zdjęte cyfry binarne.
while not stack.empty():  # Zdejmujemy reszty od ostatniej do pierwszej.
    binary_digits.append(str(stack.get()))  # Dodajemy cyfrę do wyniku.

print(f"Natural number: {number}")  # Wypisujemy liczbę wejściową.
print(f"Binary number: {''.join(binary_digits)}")  # Wypisujemy wynik binarny.
