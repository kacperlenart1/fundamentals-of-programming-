### PLIK 2.2.py: Program usuwający duplikaty z listy adresów e-mail za pomocą zbioru set.
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]  # Lista z duplikatem.
unique_emails = set(emails)  # Tworzymy zbiór, który automatycznie usuwa powtórzenia.
print(unique_emails)  # Wypisujemy unikalne adresy e-mail.
