###
# Program sprawdzający, czy nowe hasło ma co najmniej 12 znaków.
#

new_password = input('Enter new password: ')

# Sprawdzenie, czy długość hasła jest mniejsza niż 12 znaków
if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    print('Password is valid')