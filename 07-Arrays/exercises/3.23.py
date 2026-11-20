### PLIK 3.23.py: Kompletny program wywołujący wszystkie funkcje modułu MyText i wypisujący wyniki.
import MyText  # Importujemy moduł MyText.

text = "An apple a day keeps the doctor away"  # Tekst z treści zadania.
longest_list = MyText.words_longest_first(text)  # Słowa od najdłuższego do najkrótszego.
alpha_list = MyText.words_alphabetical(text)  # Słowa posortowane alfabetycznie.

print("Text:", text)  # Wypisujemy tekst.
print("Number of words:", MyText.word_count(text))  # Wypisujemy liczbę słów.
print("Words from the longest:", ",".join(longest_list))  # Wypisujemy słowa od najdłuższego.
print("Words ordered alphabetically:", ",".join(alpha_list))  # Wypisujemy słowa posortowane alfabetycznie.
