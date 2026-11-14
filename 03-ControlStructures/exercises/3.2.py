###
# Program sprawdzający poprawność loginu i hasła  z wykorzystaniem operatora logicznego 'and'.
#

login = 'joe'
password = 'abcd'

# Pobranie danych od użytkownika
entered_login = input('Login: ')
entered_password = input('Password: ')

# Sprawdzenie za pomocą operatora 'and': login i hasło muszą być poprawne jednocześnie
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')