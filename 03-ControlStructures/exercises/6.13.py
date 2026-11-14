###
# Program sprawdzający, czy prędkość samochodu mieści się w dozwolonym zakresie (40-140 km/h) na autostradzie.
#

speed_limit_min = 40
speed_limit_max = 140
car_speed = int(input("Enter car speed: "))

# Sprawdzenie, czy prędkość przekracza dozwolone limity (jest mniejsza niż min lub większa niż max)
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
else:
    print("Car speed is within the allowed limit.")