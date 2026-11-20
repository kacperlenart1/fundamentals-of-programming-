### PLIK 2.6.py: Program sprawdzający, czy użytkownik posiada wszystkie wymagane uprawnienia.
required_permissions = {"read", "write", "execute"}  # Wymagane uprawnienia.
user_permissions = {"read", "write"}  # Uprawnienia użytkownika.

has_permissions = required_permissions.issubset(user_permissions)  # Sprawdzamy, czy wymagane są podzbiorem posiadanych.
print(has_permissions)  # Wypisze False, ponieważ brakuje "execute".
