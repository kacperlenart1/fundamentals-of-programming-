### PLIK 4.7.py: Program obliczający liczbę samogłosek w podanym tekście przy użyciu wyrażeń regularnych.
import re  # Importujemy moduł wyrażeń regularnych.

text = input("Enter text: ")  # Wczytujemy dowolny tekst z klawiatury.
vowels = re.findall(r"[aeiouAEIOU]", text)  # Znajdujemy standardowe samogłoski (małe i wielkie).
print("Number of vowels:", len(vowels))  # Wypisujemy liczbę znalezionych samogłosek.
