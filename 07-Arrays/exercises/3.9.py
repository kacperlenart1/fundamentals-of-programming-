### PLIK 3.9.py: Kompletny program znajdujący najdłuższe imię z listy polskich imion.
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]  # Lista polskich imion.
longest_name = names[0]  # Zakładamy na start, że pierwsze imię jest najdłuższe.

for name in names:  # Porównujemy długość każdego imienia z aktualnie najdłuższym.
    if len(name) > len(longest_name):  # Jeśli bieżące imię ma więcej znaków.
        longest_name = name  # Zapamiętujemy nowe najdłuższe imię.

print("Names:", *names)  # Wypisujemy wszystkie imiona.
print("Longest name:", longest_name)  # Wypisujemy najdłuższe imię.
