### PLIK 2.4.py: Program znajdujący adresy spamowe wśród odebranych wiadomości (część wspólna zbiorów).
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}  # Odebrane e-maile.
spam_list = {"spam1@example.com", "spam2@example.com"}  # Znane adresy spamowe.

spam_emails = emails_received & spam_list  # Część wspólna (intersection) obu zbiorów.
print("Spam emails:", spam_emails)  # Wypisujemy znalezione adresy spamowe.
