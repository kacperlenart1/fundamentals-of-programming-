### Oblicza łączną kwotę wydatków z pliku report.txt.
import re
from decimal import Decimal
from pathlib import Path

# Ścieżka do pliku danych względem tego skryptu, także przy uruchomieniu z katalogu projektu.
email_file = Path(__file__).resolve().parent / "report.txt"

with open(email_file, "r", encoding="utf-8") as file:
    email = file.read()

# Wyszukuje kwoty w euro, również z częścią dziesiętną (np. 12.50 euro).
pattern = r"\u20ac\s*(\d+(?:[.,]\d{1,2})?)"
amounts = re.findall(pattern, email)

total = sum((Decimal(amount.replace(",", ".")) for amount in amounts), Decimal("0"))
print(f"Total money spent: \u20ac{total:.2f}")
