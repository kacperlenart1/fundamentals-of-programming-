###
# Program sprawdza, czy dana osoba jest dobrym influencerem na podstawie danych wczytanych z klawiatury.
#

facebook = input("Do you have a Facebook account? (True/False): ") == 'True'
twitter = input("Do you have a Twitter account? (True/False): ") == 'True'
instagram = input("Do you have an Instagram account? (True/False): ") == 'True'

# Sprawdzenie, czy użytkownik posiada co najmniej dwa konta w mediach społecznościowych
if int(facebook) + int(twitter) + int(instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")