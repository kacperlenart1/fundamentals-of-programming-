import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.9.py: Program wypisujący imię, nazwisko i e-mail grafików z it_company.csv z użyciem modułu csv.
import csv  # Importujemy wbudowany moduł csv.

print("GRAPHIC DESIGNERS")  # Nagłówek sekcji.
print("=================")  # Linia oddzielająca.

with open("it_company.csv", "r", encoding="utf-8", newline="") as file:  # Otwieramy plik CSV.
    reader = csv.DictReader(file)  # Wczytujemy wiersze jako słowniki na podstawie nagłówków.
    for row in reader:  # Iterujemy po rekordach pracowników.
        if row.get("Job Title", "").strip() == "Graphic Designer":  # Sprawdzamy stanowisko Graphic Designer.
            first_name = row.get("First Name", "").strip()  # Pobieramy imię.
            last_name = row.get("Last Name", "").strip()  # Pobieramy nazwisko.
            email = row.get("Email", "").strip()  # Pobieramy e-mail.
            print(f"{first_name} {last_name},{email}")  # Wypisujemy wynik w wymaganym formacie.
