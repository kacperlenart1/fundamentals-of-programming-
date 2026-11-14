###
# Program szyfrujący tekst za pomocą kodu Cezara poprzez przesunięcie każdej litery o jedną pozycję w prawo.
#

plain_text = 'The early bird catches the worm'
encrypted_text = ''

# Pętla przechodząca przez każdy znak w tekście jawnym
for char in plain_text:
    # Odczytanie kodu ASCII znaku za pomocą funkcji ord()
    char_code = ord(char)
    # Przesunięcie kodu znaku o jeden do przodu w tabeli ASCII
    encrypted_char_code = char_code + 1
    # Zamiana nowego kodu numerycznego z powrotem na znak za pomocą funkcji chr()
    encrypted_char = chr(encrypted_char_code)
    # Dodanie zaszyfrowanego znaku do ostatecznego tekstu
    encrypted_text = encrypted_text + encrypted_char

# Wyświetlenie tekstu oryginalnego oraz zaszyfrowanego
print(f'Plain text: {plain_text}')
print(f'Encrypted text: {encrypted_text}')