###
# Program sprawdzający, ile żarówek świeci się w zależności od stanu przełączników.
#

light_switch1 = False  # False - wyłącznik wyłączony, True - wyłącznik włączony
light_switch2 = False
bulbs_on = 0

# Pierwszy przełącznik włącza jedną żarówkę
if light_switch1:
    bulbs_on += 1

# Drugi przełącznik włącza pozostałe dwie żarówki
if light_switch2:
    bulbs_on += 2

# Wyświetlenie liczby świecących się żarówek
print(f"Number of bulbs on is: {bulbs_on}")