###
# Program obliczający wynagrodzenie pracownika z uwzględnieniem premii.
#

basic_salary = 5000
total_salary = 0
bonus_percentage = 0.30  # 30% premii

# Pobranie decyzji użytkownika (wpisanie 'Y' oznacza True, cokolwiek innego False)
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

# Warunek: jeśli pracownik otrzymuje premię
if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus_percentage)
else:
    total_salary = basic_salary

# Wyświetlenie podsumowania
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')