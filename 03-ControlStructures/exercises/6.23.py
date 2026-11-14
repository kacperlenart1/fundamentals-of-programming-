###
# Program tworzący tablicę mnożenia w zakresie od 1 do 10 dla dowolnej liczby wpisanej przez użytkownika.
#

number = int(input("Enter number: "))

# Pętla iterująca od 1 do 10 w celu wygenerowania i wyświetlenia kolejnych wierszy tablicy mnożenia
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")