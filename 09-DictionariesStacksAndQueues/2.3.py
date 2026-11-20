### PLIK 2.3.py: Program wyznaczający nieobecnych studentów jako różnicę zbiorów.
all_students = {"Alice", "John", "Sara", "Bob"}  # Wszyscy studenci.
attended_students = {"Alice", "Bob"}  # Studenci obecni.

absent_students = all_students - attended_students  # Różnica zbiorów: obecni w all_students, brak w attended_students.
print(absent_students)  # Wypisujemy nieobecnych studentów.
