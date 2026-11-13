###
# Program przeliczający wzrost z centymetrów na stopy i cale,
# wykorzystujący dzielenie całkowite (//) oraz resztę z dzielenia (%).
#

cm = 187

# Przeliczenie centymetrów na całkowitą liczbę cali (1 cal = 2.54 cm)
total_inches = cm / 2.54

# Obliczenie liczby stóp za pomocą operatora dzielenia bez reszty (//)
feet = int(total_inches // 12)

# Obliczenie pozostałych cali za pomocą operatora reszty z dzielenia (%)
inches = total_inches % 12

# Wyświetlenie wyniku (zaokrąglamy cale do liczby całkowitej lub 1 miejsca po przecinku)
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches:.1f} inches')