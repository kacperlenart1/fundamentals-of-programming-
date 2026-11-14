###
# Program sprawdzający, czy test został zaliczony
# (wymagane co najmniej 50% poprawnych odpowiedzi).
#

total_tasks = 20

# Pobranie liczby poprawnie rozwiązanych zadań od użytkownika
tasks_ok = int(input('Enter number of correctly completed tasks: '))

test_passed = False

# Warunek: czy liczba poprawnych zadań wynosi co najmniej 50% wszystkich zadań
if tasks_ok >= total_tasks * 0.5:
    test_passed = True

# Wyświetlenie odpowiedniego komunikatu w zależności od wyniku
if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')