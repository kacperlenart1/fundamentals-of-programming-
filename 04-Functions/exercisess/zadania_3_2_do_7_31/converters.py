### PLIK converters.py: Moduł zawierający funkcje przeliczające jednostki długości między metrami, centymetrami, calami i stopami.
def m_to_cm(n):  # Przelicza metry na centymetry mnożąc przez 100.
    return n * 100  # Zwraca wynik w centymetrach.


def cm_to_m(n):  # Przelicza centymetry na metry dzieląc przez 100.
    return n / 100  # Zwraca wynik w metrach.


def cm_to_inches(n):  # Przelicza centymetry na cale dzieląc przez 2.54.
    return n / 2.54  # Zwraca wynik w calach.


def feet_inches_to_cm(feet, inches):  # Przelicza stopy i cale na centymetry.
    return (feet * 12 + inches) * 2.54  # Zamieniamy stopy na cale (12 cali = 1 stopa), dodajemy cale i mnożymy przez 2.54.


if __name__ == "__main__":  # Blok testowy wykonuje się tylko przy bezpośrednim uruchomieniu pliku converters.py.
    print(f"2m = {m_to_cm(2)}cm")  # Test przeliczenia 2 metrów na centymetry.
    print(f"532cm = {cm_to_m(532)}m")  # Test przeliczenia 532 centymetrów na metry.
    print(f"25.4cm = {cm_to_inches(25.4)}in")  # Test przeliczenia 25.4 cm na cale.
    print(f"5ft 10in = {feet_inches_to_cm(5, 10)}cm")  # Test przeliczenia 5 stóp i 10 cali na centymetry.
