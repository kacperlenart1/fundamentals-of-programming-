###
# Program wypisujący kupon loterii z liczbami od 1 do 49 w układzie tabelarycznym.
#

for i in range(1, 8):
    for j in range(i, 50, 7):
        print(f"{j:<3}", end="")
    print()