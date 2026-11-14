###
# Program pytający użytkownika o wiek i sprawdzający, do jakiej grupy wiekowej należy.
#

age = int(input('Enter your age: '))

# Sprawdzenie przynależności do odpowiedniej grupy wiekowej na podstawie podanego wieku
if age < 13:
    group = 'Child'
elif age <= 19:
    group = 'Teen'
elif age <= 64:
    group = 'Adult'
else:
    group = 'Senior'

# Wyświetlenie ostatecznego rezultatu
print(f'You belong to the age group: {group}')