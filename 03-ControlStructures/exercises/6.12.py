###
# Program obliczający kwotę do zapłaty za zakupy z uwzględnieniem 25% rabatu na każdy produkt powyżej dwóch sztuk.
#

num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

# Obliczenie kwoty do zapłaty z uwzględnieniem rabatu na produkty powyżej dwóch sztuk
if num_products <= 2:
    total_amount = num_products * product_price
else:
    total_amount = (2 * product_price) + ((num_products - 2) * product_price * 0.75)

# Wyświetlenie ostatecznej kwoty do zapłaty
print(f"Amount to pay: {total_amount:.2f}")