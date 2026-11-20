### PLIK 3.5.py: Program sprawdzający poprawność nazwy użytkownika i hasła za pomocą wyrażeń regularnych.
import re  # Importujemy moduł re do obsługi wyrażeń regularnych.

username = input("Enter username: ")  # Wczytujemy nazwę użytkownika z klawiatury.
password = input("Enter password: ")  # Wczytujemy hasło z klawiatury.

username_pattern = r"^[a-z]{6,}$"  # Minimum 6 małych liter alfabetu łacińskiego.
password_pattern = r"^[A-Za-z0-9_]{8,}$"  # Minimum 8 znaków: litery, cyfry lub znak podkreślenia.

username_match = re.match(username_pattern, username)  # Sprawdzamy, czy login spełnia kryteria.
password_match = re.match(password_pattern, password)  # Sprawdzamy, czy hasło spełnia kryteria.

if username_match and password_match:  # Oba wzorce muszą być dopasowane.
    print("Username and password are valid.")  # Komunikat o poprawnym loginie i haśle.
else:  # Gdy któreś z kryteriów jest błędne.
    print("Invalid username or password.")  # Komunikat o niepoprawnych danych.
