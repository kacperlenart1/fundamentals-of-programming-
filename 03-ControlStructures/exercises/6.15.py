###
# Program sprawdza, czy wprowadzony numer EAN-13 ma poprawną długość i cyfry oraz czy produkt został wyprodukowany w Polsce.
#

ean = input("Enter EAN-13 article number: ")

# Sprawdzenie, czy numer składa się dokładnie z 13 cyfr
if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    
    # Sprawdzenie, czy kod zaczyna się od 590 (Polska)
    if ean.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Article number is incorrect")