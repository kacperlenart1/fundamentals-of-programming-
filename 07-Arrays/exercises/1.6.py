### PLIK 1.6.py: Kompletna funkcja weekday(n) zwracająca nazwę dnia tygodnia (1-7) oraz wypisanie dla dni 1, 4 i 7.
def weekday(n):  # Zwraca nazwę dnia tygodnia dla numeru od 1 (Monday) do 7 (Sunday).
    weekdays = [  # Lista dni tygodnia zaczynająca się od poniedziałku.
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]  # Koniec listy dni tygodnia.
    return weekdays[n - 1]  # Zwracamy element odpowiadający podanemu numerowi dnia.


print("Day 1:", weekday(1))  # Wypisujemy nazwę dnia tygodnia dla numeru 1.
print("Day 4:", weekday(4))  # Wypisujemy nazwę dnia tygodnia dla numeru 4.
print("Day 7:", weekday(7))  # Wypisujemy nazwę dnia tygodnia dla numeru 7.
