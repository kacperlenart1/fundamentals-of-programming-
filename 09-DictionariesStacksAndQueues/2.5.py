### PLIK 2.5.py: Program łączący dwie listy kontaktów i usuwający duplikaty (suma zbiorów).
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}  # Pierwszy zbiór kontaktów.
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}  # Drugi zbiór kontaktów.

merged_contacts = contacts_A | contacts_B  # Suma zbiorów (union) bez duplikatów.
print("Merged contacts:", merged_contacts)  # Wypisujemy połączone kontakty.
