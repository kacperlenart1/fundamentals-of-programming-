### PLIK icao.py: Program zamieniający kolejne litery podanego imienia na słowa alfabetu fonetycznego ICAO.
def icao(letter):  # Przyjmujemy pojedynczy znak i zwracamy odpowiadające mu słowo ICAO.
    letter = letter.capitalize()  # Zamieniamy znak na wielką literę, aby pasował do warunków if/elif.
    if letter == "A":  # Sprawdzamy literę A.
        icao_name = "Alfa"  # Przypisujemy słowo Alfa.
    elif letter == "B":  # Sprawdzamy literę B.
        icao_name = "Bravo"  # Przypisujemy słowo Bravo.
    elif letter == "C":  # Sprawdzamy literę C.
        icao_name = "Charlie"  # Przypisujemy słowo Charlie.
    elif letter == "D":  # Sprawdzamy literę D.
        icao_name = "Delta"  # Przypisujemy słowo Delta.
    elif letter == "E":  # Sprawdzamy literę E.
        icao_name = "Echo"  # Przypisujemy słowo Echo.
    elif letter == "F":  # Sprawdzamy literę F.
        icao_name = "Foxtrot"  # Przypisujemy słowo Foxtrot.
    elif letter == "G":  # Sprawdzamy literę G.
        icao_name = "Golf"  # Przypisujemy słowo Golf.
    elif letter == "H":  # Sprawdzamy literę H.
        icao_name = "Hotel"  # Przypisujemy słowo Hotel.
    elif letter == "I":  # Sprawdzamy literę I.
        icao_name = "India"  # Przypisujemy słowo India.
    elif letter == "J":  # Sprawdzamy literę J.
        icao_name = "Juliett"  # Przypisujemy słowo Juliett.
    elif letter == "K":  # Sprawdzamy literę K.
        icao_name = "Kilo"  # Przypisujemy słowo Kilo.
    elif letter == "L":  # Sprawdzamy literę L.
        icao_name = "Lima"  # Przypisujemy słowo Lima.
    elif letter == "M":  # Sprawdzamy literę M.
        icao_name = "Mike"  # Przypisujemy słowo Mike.
    elif letter == "N":  # Sprawdzamy literę N.
        icao_name = "November"  # Przypisujemy słowo November.
    elif letter == "O":  # Sprawdzamy literę O.
        icao_name = "Oscar"  # Przypisujemy słowo Oscar.
    elif letter == "P":  # Sprawdzamy literę P.
        icao_name = "Papa"  # Przypisujemy słowo Papa.
    elif letter == "Q":  # Sprawdzamy literę Q.
        icao_name = "Quebec"  # Przypisujemy słowo Quebec.
    elif letter == "R":  # Sprawdzamy literę R.
        icao_name = "Romeo"  # Przypisujemy słowo Romeo.
    elif letter == "S":  # Sprawdzamy literę S.
        icao_name = "Sierra"  # Przypisujemy słowo Sierra.
    elif letter == "T":  # Sprawdzamy literę T.
        icao_name = "Tango"  # Przypisujemy słowo Tango.
    elif letter == "U":  # Sprawdzamy literę U.
        icao_name = "Uniform"  # Przypisujemy słowo Uniform.
    elif letter == "V":  # Sprawdzamy literę V.
        icao_name = "Victor"  # Przypisujemy słowo Victor.
    elif letter == "W":  # Sprawdzamy literę W.
        icao_name = "Whiskey"  # Przypisujemy słowo Whiskey.
    elif letter == "X":  # Sprawdzamy literę X.
        icao_name = "X-ray"  # Przypisujemy słowo X-ray.
    elif letter == "Y":  # Sprawdzamy literę Y.
        icao_name = "Yankee"  # Przypisujemy słowo Yankee.
    elif letter == "Z":  # Sprawdzamy literę Z.
        icao_name = "Zulu"  # Przypisujemy słowo Zulu.
    else:  # Dla znaków spoza alfabetu łacińskiego A-Z.
        icao_name = "???"  # Zwracamy znaki zapytania.

    return icao_name  # Zwracamy wyznaczone słowo ICAO.


name = input("Enter your name: ")  # Wczytujemy imię wpisane przez użytkownika z klawiatury.
print("ICAO words for spelling out your name:")  # Wypisujemy nagłówek przed listą słów ICAO.

for char in name:  # Przechodzimy po każdym znaku w zmiennej name.
    word = icao(char)  # Wywołujemy funkcję icao dla bieżącego znaku char.
    print(word, end=" ")  # Wypisujemy słowo ICAO i oddzielamy spacją zamiast przechodzić do nowej linii.
