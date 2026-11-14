###
# Program sprawdzający, czy samochód przekroczył dozwoloną prędkość na autostradzie.
#

speed_limit = 140
car_speed = int(input('Enter car speed (km/h): '))

# Warunek: czy prędkość samochodu przekracza limit
if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')