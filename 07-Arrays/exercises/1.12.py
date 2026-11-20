### PLIK 1.12.py: Kompletny program wskazujący najbardziej kosztowną kategorię wydatków w miesiącu.
categories = ["Food", "Transport", "Rent", "Entertainment"]  # Lista kategorii wydatków.
expenses = [500, 150, 1000, 200]  # Kwoty wydatków odpowiadające kategoriom.

max_index = 0  # Indeks kategorii z najwyższym wydatkiem na starcie.
for i in range(1, len(expenses)):  # Przeglądamy pozostałe kwoty.
    if expenses[i] > expenses[max_index]:  # Porównujemy bieżący wydatek z dotychczasowym maksimum.
        max_index = i  # Zapamiętujemy indeks wyższego wydatku.

print("Most expensive category:", categories[max_index])  # Wypisujemy najbardziej kosztowną kategorię.
print("Highest expense:", expenses[max_index])  # Wypisujemy kwotę tego wydatku.
