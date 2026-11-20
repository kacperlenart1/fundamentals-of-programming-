### PLIK 1.8.py: Kompletny program sortujący gry alfabetycznie i wypisujący je ponumerowane w pętli while.
computer_games = [  # Lista popularnych gier komputerowych.
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]  # Koniec listy gier.

sorted_games = sorted(computer_games)  # Sortujemy listę alfabetycznie wbudowaną funkcją sorted().
counter = 0  # Zmienna licznikowa używana w pętli while.
while counter < len(sorted_games):  # Pętla wykonuje się dla wszystkich elementów posortowanej listy.
    print(f"{counter + 1}. {sorted_games[counter]}")  # Wypisujemy numer kolejny oraz nazwę gry.
    counter += 1  # Zwiększamy licznik o 1.
