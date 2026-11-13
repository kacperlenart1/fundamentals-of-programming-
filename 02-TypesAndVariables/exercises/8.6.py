###
# Program obliczający całkowity koszt transportu towarów na podstawie podanej odległości, ceny paliwa i zużycia paliwa na 100 km.
#

# Pobranie danych od użytkownika
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))

# Obliczenie całkowitego zużycia paliwa
total_fuel_consumption = (distance * fuel_consumption) / 100

# Obliczenie całkowitego kosztu transportu
total_cost = total_fuel_consumption * fuel_price

# Wyświetlenie wyników (z zaokrągleniem do 2 miejsc po przecinku)
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')
print(f'Total transport cost: {total_cost:.2f}')