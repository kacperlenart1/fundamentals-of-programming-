### PLIK emails.py: Moduł z funkcjami wyciągającymi nadawcę, odbiorcę, temat oraz treść wiadomości e-mail.
import re  # Importujemy moduł wyrażeń regularnych.


def email_sender(content):  # Zwraca adres e-mail nadawcy z nagłówka From.
    match = re.search(r"^From:.*<([^>\s]+@[^>\s]+)>", content, re.MULTILINE)  # Szukamy adresu w nawiasach ostrokątnych.
    if match:  # Jeśli znaleziono adres w nawiasach.
        return match.group(1)  # Zwracamy sam adres e-mail.
    plain_match = re.search(r"^From:\s*([^\s<>]+@[^\s<>]+)", content, re.MULTILINE)  # Szukamy samego adresu po From:.
    return plain_match.group(1) if plain_match else ""  # Zwracamy adres lub pusty napis.


def email_recipient(content):  # Zwraca adres e-mail odbiorcy z nagłówka To.
    match = re.search(r"^To:.*<([^>\s]+@[^>\s]+)>", content, re.MULTILINE)  # Szukamy adresu odbiorcy w nawiasach.
    if match:  # Jeśli znaleziono adres w nawiasach.
        return match.group(1)  # Zwracamy adres odbiorcy.
    plain_match = re.search(r"^To:\s*([^\s<>]+@[^\s<>]+)", content, re.MULTILINE)  # Szukamy samego adresu po To:.
    return plain_match.group(1) if plain_match else ""  # Zwracamy adres lub pusty napis.


def email_subject(content):  # Zwraca temat wiadomości z nagłówka Subject.
    match = re.search(r"^Subject:\s*(.+)$", content, re.MULTILINE)  # Wyciągamy cały tekst po Subject:.
    return match.group(1).strip() if match else ""  # Zwracamy oczyszczony temat lub pusty napis.


def email_body(content):  # Zwraca treść wiadomości e-mail (po pustej linii oddzielającej nagłówki).
    match = re.search(r"\r?\n\r?\n(.*)$", content, re.DOTALL)  # Pobieramy wszystko po pierwszej pustej linii.
    return match.group(1).strip() if match else ""  # Zwracamy treść e-maila bez zbędnych skrajnych spacji/enterów.
