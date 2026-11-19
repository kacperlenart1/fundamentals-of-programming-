### PLIK 4.8.py: Funkcja zamieniająca godzinę i minuty na napis w formacie 24-godzinnym lub 12-godzinnym.
def time_string(hours, minutes, time_format):  # Definiujemy funkcję formatującą czas dla godzin, minut i wybranego formatu.
    if time_format == "24":  # Obsługujemy zapis w standardzie 24-godzinnym.
        return f"{hours:02d}:{minutes:02d}"  # Dopełniamy godziny i minuty zerem z przodu tak, aby miały po dwie cyfry.
    elif time_format == "12":  # Obsługujemy zapis w standardzie 12-godzinnym z przyrostkiem am lub pm.
        period = "am" if hours < 12 else "pm"  # Godziny poniżej 12 oznaczamy jako am, a od 12 w górę jako pm.
        hour_12 = hours % 12  # Przeliczamy godzinę na zakres od 0 do 11.
        if hour_12 == 0:  # W formacie 12-godzinnym godzinę 0 lub 12 zapisujemy jako 12.
            hour_12 = 12  # Ustawiamy godzinę na 12.
        return f"{hour_12}:{minutes:02d}{period}"  # Zwracamy sformatowany czas w systemie 12-godzinnym.
    return ""  # Zwracamy pusty napis, jeśli podano nieznany format czasu.


print(time_string(15, 38, "24"))  # Spodziewany wynik: 15:38.
print(time_string(8, 3, "24"))  # Spodziewany wynik: 08:03.
print(time_string(0, 5, "24"))  # Spodziewany wynik: 00:05.
print(time_string(11, 15, "12"))  # Spodziewany wynik: 11:15am.
print(time_string(0, 7, "12"))  # Spodziewany wynik: 12:07am.
print(time_string(7, 30, "12"))  # Spodziewany wynik: 7:30am.
print(time_string(12, 46, "12"))  # Spodziewany wynik: 12:46pm.
print(time_string(13, 10, "12"))  # Spodziewany wynik: 1:10pm.
print(time_string(19, 2, "12"))  # Spodziewany wynik: 7:02pm.
