###
# Program konwertujący czas z formatu 24-godzinnego na 12-godzinny.
#

time_24 = input("Enter time (24-hour format): ")

# Podział wczytanego ciągu znaków na godziny i minuty
hours = int(time_24[:2])
minutes = time_24[3:]

# Ustalenie sufiksu am/pm oraz odpowiednie przeliczenie godzin
if hours >= 12:
    period = "pm"
    if hours > 12:
        hours -= 12
else:
    period = "am"
    if hours == 0:
        hours = 12

# Wyświetlenie czasu w formacie 12-godzinnym
print(f"Time in 12-hour format: {hours}:{minutes}{period}")