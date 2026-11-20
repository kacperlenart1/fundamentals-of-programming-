### PLIK 5.3.py: Program tłumaczący podane angielskie słowo na język polski na podstawie słownika.
translations = {  # Słownik tłumaczeń angielski -> polski.
    "computer": "komputer",
    "mouse": "myszka",
    "keyboard": "klawiatura",
    "printer": "drukarka",
}  # Koniec słownika.

word = input("Enter English word: ").strip().lower()  # Wczytujemy słowo i normalizujemy wielkość liter.

if word in translations:  # Sprawdzamy, czy słowo znajduje się w słowniku.
    print("Translation:", translations[word])  # Wypisujemy tłumaczenie.
else:  # Gdy tłumaczenia brak w słowniku.
    print("Translation is unavailable.")  # Informujemy o braku tłumaczenia.
