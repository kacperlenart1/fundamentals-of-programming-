### PLIK 7.15.py: Funkcja sprawdzająca czy stan osób w pokoju osiągnął co najmniej 3 na podstawie zdarzeń + i -.
def f(detector):  # Przyjmujemy sekwencję wejść (+) i wyjść (-).
    people = 0  # Aktualna liczba osób w pokoju.
    for ch in detector:  # Przechodzimy po każdym zdarzeniu w napisie.
        if ch == "+":  # Wejście osoby do pokoju.
            people += 1  # Zwiększamy liczbę osób o 1.
        elif ch == "-":  # Wyjście osoby z pokoju.
            people -= 1  # Zmniejszamy liczbę osób o 1.
        if people >= 3:  # Jeśli w którymś momencie w pokoju są co najmniej 3 osoby.
            return True  # Od razu zwracamy True.
    return False  # Jeśli nigdy nie było jednocześnie 3 osób, zwracamy False.


print(f("+-+++-+---"))  # Zwróci True.
print(f("+-+-+-+-"))  # Zwróci False.
print(f("+-++-+--"))  # Zwróci False.
print(f("+-++-++-+---"))  # Zwróci True.
