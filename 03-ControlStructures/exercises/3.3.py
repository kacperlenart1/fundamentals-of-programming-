###
# Program sprawdzający, czy osoba o podanym wieku jest uprawniona do zniżki (wiek < 18 lub wiek >= 65).
#

age = int(input('Enter your age: '))

# Sprawdzenie warunku za pomocą operatora 'or'
if age < 18 or age >= 65:
    print(f'A person aged {age} is eligible for the discount')
else:
    print(f'A person aged {age} is not eligible for the discount')