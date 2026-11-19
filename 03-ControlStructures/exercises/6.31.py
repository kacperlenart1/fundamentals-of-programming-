###
# Program generujący i wypisujący 20 losowych liczb całkowitych z zakresu od 5 do 10.
#

import random

# Pętla wykonująca się 20 razy, losująca i wypisująca liczby z przedziału [5, 10]
for _ in range(20):
    print(random.randint(5, 10), end=" ")

print()