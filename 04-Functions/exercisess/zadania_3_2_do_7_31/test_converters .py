### PLIK test_converters.py: Program importujący moduł converters i testujący jego funkcje przeliczające.
import converters  # Importujemy własny moduł converters z tego samego folderu.

print("### Test converters")  # Wypisujemy nagłówek testów.
print(f"Three meters is {converters.m_to_cm(3)}cm")  # Wywołujemy funkcję m_to_cm z modułu converters dla 3 metrów.
print(f"50.8 cm is {converters.cm_to_inches(50.8)} inches")  # Wywołujemy funkcję cm_to_inches z modułu converters.
print(f"6 feet 0 inches is {converters.feet_inches_to_cm(6, 0)} cm")  # Wywołujemy funkcję feet_inches_to_cm z modułu converters.
