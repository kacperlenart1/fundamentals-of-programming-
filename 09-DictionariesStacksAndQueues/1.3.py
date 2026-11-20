### PLIK 1.3.py: Słownik opisujący telefon (6 par klucz-wartość) wypisany w pętli for.
mobile = {  # Tworzymy słownik z 6 cechami telefonu.
    "OS": "Android",
    "brand": "Samsung",
    "model": "Galaxy S24",
    "ram_gb": 12,
    "storage_gb": 256,
    "dual_sim": True,
}  # Koniec słownika.

for key, value in mobile.items():  # Przechodzimy przez wszystkie pary klucz-wartość.
    print(f"{key} : {value}")  # Wypisujemy klucz i przypisaną mu wartość.
