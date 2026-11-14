###
# Program obliczający całkowite zużycie paliwa na podstawie trybu jazdy i przebytej odległości.
#

driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

# Określenie spalania na 100 km w zależności od trybu jazdy
if driving_mode == 'A':
    fuel_consumption = 7
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6
else:
    fuel_consumption = 0  # Wartość domyślna w razie podania niepoprawnego trybu

# Obliczenie całkowitego zużycia paliwa
total_consumption = (distance * fuel_consumption) / 100

# Wyświetlenie wyniku
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')