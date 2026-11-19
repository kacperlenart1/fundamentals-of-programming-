### PLIK 4.4.py: Funkcja zwracająca sumę cyfr podanej liczby całkowitej z uwzględnieniem liczb ujemnych.
def sum_digits(number):  # Definiujemy funkcję przyjmującą liczbę całkowitą number.
    total = 0  # Tworzymy zmienną akumulator, w której będziemy sumować kolejne cyfry.
    for ch in str(abs(number)):  # Bierzemy wartość bezwzględną liczby, zamieniamy na tekst i przechodzimy po każdym znaku.
        total += int(ch)  # Zamieniamy pojedynczy znak z powrotem na int i dodajemy do sumy.
    return total  # Zwracamy łączną sumę wszystkich cyfr.


any_number = int(input("Enter integer number: "))  # Pobieramy od użytkownika liczbę całkowitą z klawiatury.
result = sum_digits(any_number)  # Wywołujemy funkcję sum_digits i zapisujemy wynik.
print(f"The sum of the digits in the number {any_number} is {result}")  # Wyświetlamy końcową sumę cyfr.
