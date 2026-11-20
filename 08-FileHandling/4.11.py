import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.11.py: Program obliczający, wypisujący i zapisujący do pliku liczby 1..100 oraz ich 2. i 3. potęgę.
output_file = "powers.txt"  # Nazwa pliku, do którego zapiszemy wyniki.

with open(output_file, "w", encoding="utf-8") as file:  # Otwieramy plik do zapisu.
    for number in range(1, 101):  # Przechodzimy przez liczby całkowite od 1 do 100.
        row_text = f"{number},{number ** 2},{number ** 3}"  # Tworzymy linię: liczba, kwadrat, sześcian.
        print(row_text)  # Wypisujemy linię w terminalu.
        file.write(f"{row_text}\n")  # Zapisujemy linię do pliku tekstowego.
