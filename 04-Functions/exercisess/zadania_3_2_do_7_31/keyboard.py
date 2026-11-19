### PLIK keyboard.py: Moduł pomocniczy do bezpiecznego wczytywania danych różnych typów z klawiatury.
def input_string(message):  # Wczytuje zwykły tekst z komunikatem message.
    value = input(message)  # Pobieramy napis od użytkownika.
    return value  # Zwracamy wczytany napis.


def input_integer(message):  # Wczytuje liczbę całkowitą z klawiatury.
    value = int(input(message))  # Zamieniamy wpisany tekst na typ int.
    return value  # Zwracamy liczbę całkowitą.


def input_real(message):  # Wczytuje liczbę zmiennoprzecinkową z klawiatury.
    value = float(input(message))  # Zamieniamy wpisany tekst na typ float.
    return value  # Zwracamy liczbę rzeczywistą.


def input_boolean(message):  # Wczytuje odpowiedź tak lub nie jako wartość logiczną bool.
    value = input(message).strip().lower()  # Usuwamy zbędne spacje i zamieniamy na małe litery.
    return value == "y"  # Zwracamy True gdy użytkownik wpisał y, a w przeciwnym razie False.
