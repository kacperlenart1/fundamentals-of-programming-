###
# Program konwertujący liczbę dziesiętną na postać binarną za pomocą kolejnych dzieleń przez 2.
#

decimal_number = int(input("Enter decimal number: "))
original_number = decimal_number
binary_number = ""

# Obsługa przypadku, gdy podana liczba wynosi zero
if decimal_number == 0:
    binary_number = "0"
else:
    # Pętla wykonująca dzielenie przez 2 aż do uzyskania ilorazu równego zero
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2

# Wyświetlenie ostatecznego wyniku w formacie dziesiętnym i binarnym
print(f"{original_number}(10) = {binary_number}(2)")