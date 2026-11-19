### PLIK 7.27.py: Funkcja sprawdzająca czy czwarta cyfra kodu jest resztą z dzielenia sumy pierwszych trzech cyfr przez 7.
def f(product_code):  # Przyjmujemy kod produktu jako napis.
    if len(product_code) != 4 or not product_code.isdigit():  # Kod musi mieć dokładnie 4 znaki i składać się z samych cyfr.
        return False  # Zwracamy False, gdy format kodu jest niepoprawny.
    first_three_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])  # Sumujemy pierwsze trzy cyfry.
    check_digit = first_three_sum % 7  # Wyliczamy cyfrę kontrolną jako resztę z dzielenia przez 7.
    return int(product_code[3]) == check_digit  # Porównujemy czwartą cyfrę kodu z wyliczoną cyfrą kontrolną.


print(f("1082"))  # Suma 1+0+8 = 9, 9 % 7 = 2, zgadza się z czwartą cyfrą -> True.
print(f("2035"))  # Suma 2+0+3 = 5, 5 % 7 = 5, zgadza się z czwartą cyfrą -> True.
print(f("1114"))  # Suma 1+1+1 = 3, 3 % 7 = 3 != 4 -> False.
print(f("7071"))  # Suma 7+0+7 = 14, 14 % 7 = 0 != 1 -> False.
