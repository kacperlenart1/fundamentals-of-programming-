import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.19.py: Program podsumowujący rezerwacje z reservations.json z podziałem na funkcje.
import json  # Importujemy moduł json.


def load_reservations(file_path):  # Wczytuje listę rezerwacji z pliku JSON.
    with open(file_path, "r", encoding="utf-8") as file:  # Otwieramy plik reservations.json.
        data = json.load(file)  # Wczytujemy strukturę JSON.
    return data.get("reservations", [])  # Zwracamy listę rezerwacji.


def reservation_amount(reservation):  # Oblicza wartość pojedynczej rezerwacji (noce * cena za noc).
    return reservation.get("nights", 0) * reservation.get("price_per_night", 0.0)  # Zwracamy kwotę rezerwacji.


def summarize_reservations(reservations):  # Wyznacza statystyki rezerwacji opłaconych i nieopłaconych.
    paid_count = 0  # Liczba opłaconych rezerwacji.
    unpaid_count = 0  # Liczba nieopłaconych rezerwacji.
    paid_total = 0.0  # Łączna wartość opłaconych rezerwacji.
    unpaid_total = 0.0  # Łączna wartość nieopłaconych rezerwacji.

    for res in reservations:  # Przechodzimy przez wszystkie rezerwacje.
        amount = reservation_amount(res)  # Liczymy wartość danej rezerwacji.
        if res.get("paid"):  # Jeśli rezerwacja jest opłacona.
            paid_count += 1  # Zwiększamy licznik opłaconych.
            paid_total += amount  # Dodajemy kwotę do sumy opłaconych.
        else:  # Jeśli rezerwacja jest nieopłacona.
            unpaid_count += 1  # Zwiększamy licznik nieopłaconych.
            unpaid_total += amount  # Dodajemy kwotę do sumy nieopłaconych.

    return {  # Zwracamy słownik z podsumowaniem.
        "rooms_count": len(reservations),
        "paid_count": paid_count,
        "unpaid_count": unpaid_count,
        "paid_total": paid_total,
        "unpaid_total": unpaid_total,
    }


def main():  # Główna funkcja programu.
    reservations = load_reservations("reservations.json")  # Wczytujemy rezerwacje.
    summary = summarize_reservations(reservations)  # Liczymy podsumowanie.

    print("Number of rooms:", summary["rooms_count"])  # Wypisujemy liczbę rezerwacji/pokoi.
    print("Number of paid reservations:", summary["paid_count"])  # Wypisujemy liczbę opłaconych.
    print("Number of unpaid reservations:", summary["unpaid_count"])  # Wypisujemy liczbę nieopłaconych.
    print(f"Total value of paid reservations: {summary['paid_total']:.2f}")  # Suma opłaconych.
    print(f"Total value of unpaid reservations: {summary['unpaid_total']:.2f}")  # Suma nieopłaconych.


if __name__ == "__main__":  # Uruchamiamy main() tylko przy bezpośrednim wywołaniu pliku.
    main()  # Wywołujemy funkcję główną.
