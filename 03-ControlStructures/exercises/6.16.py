###
# Program obliczający całkowity czas prania na podstawie wybranego programu oraz opcji dodatkowych.
#

total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

# Określenie czasu prania w zależności od wybranego programu
if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20

# Dodanie czasu za dodatkowe płukanie, jeśli wybrano 'y'
if extra_rinse == 'y':
    total_washing_time += 15

# Dodanie czasu za dodatkowe wirowanie, jeśli wybrano 'y'
if extra_spin == 'y':
    total_washing_time += 9

# Wyświetlenie całkowitego czasu prania
print(f"Total washing time: {total_washing_time} minutes")