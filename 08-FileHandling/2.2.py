import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 2.2.py: Program zapisujący Siedem Cudów Świata w kolejności alfabetycznej do pliku seven_wonders.txt.
seven_wonders = [  # Lista Siedmiu Cudów Świata.
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]  # Koniec listy.

file_name = 'seven_wonders.txt'  # Nazwa pliku docelowego.
sorted_wonders = sorted(seven_wonders)  # Sortujemy listę alfabetycznie za pomocą sorted().

with open(file_name, 'w', encoding='utf-8') as file:  # Otwieramy plik w trybie zapisu ('w').
    for item in sorted_wonders:  # Iterujemy po posortowanych elementach.
        file.write(f"{item}\n")  # Zapisujemy każdy element w osobnej linii.
