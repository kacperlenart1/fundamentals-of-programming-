import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.5.py: Program odczytujący email.txt i wypisujący nadawcę, odbiorcę, temat i treść z użyciem modułu emails.
import emails  # Importujemy własny moduł emails.py.

with open("email.txt", "r", encoding="utf-8") as file:  # Otwieramy plik email.txt.
    email_content = file.read()  # Wczytujemy całą zawartość pliku.

print("Sender:", emails.email_sender(email_content))  # Wypisujemy adres nadawcy.
print("Recipient:", emails.email_recipient(email_content))  # Wypisujemy adres odbiorcy.
print("Subject:", emails.email_subject(email_content))  # Wypisujemy temat wiadomości.
print("Body:\n" + emails.email_body(email_content))  # Wypisujemy treść wiadomości.
