### PLIK 1.9.py: Kompletny program wypisujący ponumerowane tablice rejestracyjne z Krakowa (zaczynające się na KR lub KK).
polish_license_plates = [  # Lista polskich tablic rejestracyjnych.
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]  # Koniec listy tablic.

counter = 1  # Numer porządkowy dla znalezionych rejestracji z Krakowa.
for car_number in polish_license_plates:  # Przechodzimy przez wszystkie tablice rejestracyjne.
    if car_number.startswith("KR") or car_number.startswith("KK"):  # Sprawdzamy czy rejestracja jest z Krakowa.
        print(f"{counter}. {car_number}")  # Wypisujemy numer na liście oraz tablicę rejestracyjną.
        counter += 1  # Zwiększamy numer porządkowy o 1.
