### PLIK 4.6.py: Funkcja zwracająca angielską nazwę dnia tygodnia na podstawie jego numeru od 1 do 7.
def day_name(day_number):  # Definiujemy funkcję przyjmującą numer dnia tygodnia.
    result = ""  # Przygotowujemy zmienną przechowującą nazwę dnia.
    if day_number == 1:  # Sprawdzamy czy to pierwszy dzień tygodnia.
        result = "Monday"  # Zwracamy nazwę poniedziałku po angielsku.
    elif day_number == 2:  # Sprawdzamy czy to drugi dzień tygodnia.
        result = "Tuesday"  # Zwracamy nazwę wtorku po angielsku.
    elif day_number == 3:  # Sprawdzamy czy to trzeci dzień tygodnia.
        result = "Wednesday"  # Zwracamy nazwę środy po angielsku.
    elif day_number == 4:  # Sprawdzamy czy to czwarty dzień tygodnia.
        result = "Thursday"  # Zwracamy nazwę czwartku po angielsku.
    elif day_number == 5:  # Sprawdzamy czy to piąty dzień tygodnia.
        result = "Friday"  # Zwracamy nazwę piątku po angielsku.
    elif day_number == 6:  # Sprawdzamy czy to szósty dzień tygodnia.
        result = "Saturday"  # Zwracamy nazwę soboty po angielsku.
    elif day_number == 7:  # Sprawdzamy czy to siódmy dzień tygodnia.
        result = "Sunday"  # Zwracamy nazwę niedzieli po angielsku.
    return result  # Zwracamy wybraną nazwę dnia lub pusty napis, jeśli numer był spoza zakresu 1..7.


print("The name of day 5 in the week is", day_name(5))  # Wypisujemy nazwę dla dnia numer 5.
print("The name of day 3 in the week is", day_name(3))  # Wypisujemy nazwę dla dnia numer 3.
print("The name of day 7 in the week is", day_name(7))  # Wypisujemy nazwę dla dnia numer 7.
