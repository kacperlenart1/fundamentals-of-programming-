###
# Program obliczający wiek psa w psie latach na podstawie podanego wieku w latach ludzkich.
#

human_years = int(input("Enter the dog's age in human years: "))

# Obliczenie wieku psa w psie latach zgodnie z przyjętymi regułami
if human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4

# Wyświetlenie ostatecznego wyniku w psie latach
print(f"The dog's age in dog's years is {int(dog_years)} years.")