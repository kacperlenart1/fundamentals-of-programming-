import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 2.5.py: Program dopisujący kolejne produkty wpisane z klawiatury do pliku shopping_list.txt aż do wpisania 0.
shopping_list = 'shopping_list.txt'  # Nazwa pliku z listą zakupów.


def add_product(file_name, product_name):  # Dopisuje nazwę produktu na końcu wskazanego pliku.
    with open(file_name, 'a', encoding='utf-8') as file:  # Otwieramy plik w trybie dopisywania ('a').
        file.write(f"{product_name}\n")  # Zapisujemy nazwę produktu i przechodzimy do nowej linii.


product = ""  # Zmienna przechowująca bieżącą nazwę produktu.
while product != "0":  # Pętla działa dopóki użytkownik nie wpisze zera.
    product = input('Enter product name (0 stops): ')  # Pobieramy nazwę produktu z klawiatury.
    if product == '0':  # Sprawdzamy, czy użytkownik chce zakończyć wpisywanie.
        break  # Przerywamy pętlę while.
    else:  # W przeciwnym razie dopisujemy produkt do pliku.
        add_product(shopping_list, product)  # Wywołujemy funkcję dopisującą produkt do pliku.
