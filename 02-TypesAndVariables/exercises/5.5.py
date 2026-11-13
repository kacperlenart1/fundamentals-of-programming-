###
# Program obliczający cenę produktu po uwzględnieniu rabatu
#

# Pobranie ceny i procentu rabatu od użytkownika
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

# Obliczenie wysokości obniżki oraz ceny po rabacie
reduction = price * (discount / 100)
price_with_discount = price - reduction

# Wyświetlenie wyników z formatowaniem do dwóch miejsc po przecinku
print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")