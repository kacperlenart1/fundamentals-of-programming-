###
# Program klasyfikujący wiek użytkownika na podstawie instrukcji elif.
#

age = int(input('Enter age: '))

if age < 13:
    print('Child')
elif age < 20:
    print('Teenager')
elif age < 65:
    print('Adult')
else:
    print('Senior')