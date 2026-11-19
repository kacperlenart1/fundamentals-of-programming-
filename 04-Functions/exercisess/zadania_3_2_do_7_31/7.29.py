### PLIK 7.29.py: Program obliczający silnię liczby n rekurencyjnie i wypisujący wynik dla n równego 5.
def factorial(n):  # Funkcja wywołująca samą siebie w celu obliczenia n!.
    if n == 0 or n == 1:  # Warunek bazowy rekurencji: 0! = 1 oraz 1! = 1.
        return 1  # Kończymy schodzenie w głąb rekurencji i zwracamy 1.
    if n > 1:  # Dla liczb większych od 1 korzystamy ze wzoru n * (n - 1)!.
        return n * factorial(n - 1)  # Mnożymy n przez wynik rekurencyjnego wywołania dla n - 1.


print(factorial(5))  # 5! = 5 * 4 * 3 * 2 * 1 = 120.
