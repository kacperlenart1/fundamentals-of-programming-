### Polecenie: sprawdza, czy podana liczba występuje w tablicy.
def occurs(number, array):  # Zwraca True, jeśli liczba znajduje się w tablicy.
    for item in array:  # Sprawdzamy kolejno elementy tablicy.
        if item == number:  # Gdy znajdziemy szukaną liczbę.
            return True  # Zwracamy informację o jej obecności.
    return False  # Liczby nie ma w tablicy.


number = int(input("Number: "))  # Wczytujemy liczbę od użytkownika.
numbers = [15, 38, 7, 23, 14]  # Tablica podana w poleceniu.

print("Array:", *numbers)  # Wypisujemy tablicę.
if occurs(number, numbers):  # Sprawdzamy obecność liczby.
    print(f"Result: number {number} appears in the array")  # Informujemy, że liczba została znaleziona.
else:
    print(f"Result: number {number} does not appear in the array")  # Informujemy, że liczby nie ma w tablicy.
