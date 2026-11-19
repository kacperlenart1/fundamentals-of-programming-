###
# Program analizujący spadek ceny produktu i wyświetlający rekomendację zakupu, jeśli cena spadła o co najmniej 10%.
#

current_price = 140.00
previous_price = 200.00

# Obliczenie procentowego spadku ceny produktu
price_drop_percentage = ((previous_price - current_price) / previous_price) * 100

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

# Sprawdzenie, czy cena spadła o co najmniej 10%
if price_drop_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(price_drop_percentage)}%")