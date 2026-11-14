###
# Program symulujący termometr elektroniczny, który wyświetla temperaturę oraz odpowiedni komunikat tekstowy.
#

temp = float(input('Enter temperature in Celsius: '))

# Sprawdzenie warunków temperaturowych w odpowiedniej kolejności
if temp > 35:
    message = 'It is extremely hot'
elif temp > 30:
    message = 'It is hot'
elif temp >= 15:
    message = 'It is warm'
elif temp >= 0:
    message = 'It is cold'
else:
    message = 'Warning, frost'

# Wyświetlenie temperatury oraz opisu słownego
print(f'Temperature: {temp}°C. {message}')