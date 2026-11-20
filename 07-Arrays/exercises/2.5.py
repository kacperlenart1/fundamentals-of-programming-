### PLIK 2.5.py: Kompletny program obliczający łączną liczbę miejsc, wolne i zajęte fotele oraz status wybranych miejsc w kinie.
cinema_seats = [  # Układ miejsc w kinie 5x5 ('A' = wolne, 'B' = zajęte).
    ['A', 'A', 'B', 'A', 'A'],  # Rząd 1.
    ['A', 'B', 'B', 'A', 'A'],  # Rząd 2.
    ['A', 'A', 'A', 'A', 'B'],  # Rząd 3.
    ['B', 'A', 'A', 'A', 'A'],  # Rząd 4.
    ['A', 'B', 'A', 'A', 'A']   # Rząd 5.
]  # Koniec układu sali.


def seats_total(seats):  # Zwraca całkowitą liczbę miejsc na sali kinowej.
    total = 0  # Licznik wszystkich miejsc.
    for row in seats:  # Przechodzimy po każdym rzędzie.
        total += len(row)  # Dodajemy liczbę miejsc w rzędzie.
    return total  # Zwracamy łączną liczbę miejsc.


def seats_available(seats):  # Zwraca liczbę wolnych miejsc oznaczonych jako 'A'.
    available = 0  # Licznik wolnych miejsc.
    for row in seats:  # Przechodzimy po każdym rzędzie.
        for seat in row:  # Sprawdzamy każde miejsce w rzędzie.
            if seat == 'A':  # Gdy miejsce jest wolne.
                available += 1  # Zwiększamy licznik wolnych miejsc.
    return available  # Zwracamy liczbę wolnych miejsc.


def seats_booked(seats):  # Zwraca liczbę zajętych miejsc oznaczonych jako 'B'.
    booked = 0  # Licznik zajętych miejsc.
    for row in seats:  # Przechodzimy po każdym rzędzie.
        for seat in row:  # Sprawdzamy każde miejsce w rzędzie.
            if seat == 'B':  # Gdy miejsce jest zajęte.
                booked += 1  # Zwiększamy licznik zajętych miejsc.
    return booked  # Zwracamy liczbę zajętych miejsc.


def seat_status(seats, row, place):  # Zwraca tekstowy status miejsca dla podanego rzędu i miejsca (od 1).
    if seats[row - 1][place - 1] == 'A':  # Sprawdzamy czy miejsce jest wolne.
        return "Available"  # Miejsce wolne.
    return "Booked"  # Miejsce zajęte.


print("CINEMA INFORMATION TABLE")  # Nagłówek raportu.
print("Total seats:", seats_total(cinema_seats))  # Łączna liczba miejsc.
print("Seats available:", seats_available(cinema_seats))  # Liczba wolnych miejsc.
print("Seats booked:", seats_booked(cinema_seats))  # Liczba zajętych miejsc.
print("Seat in row 1, place 1:", seat_status(cinema_seats, 1, 1))  # Status miejsca w rzędzie 1, miejsce 1.
print("Seat in row 5, place 5:", seat_status(cinema_seats, 5, 5))  # Status miejsca w rzędzie 5, miejsce 5.
print("Seat in row 3, place 5:", seat_status(cinema_seats, 3, 5))  # Status miejsca w rzędzie 3, miejsce 5.
