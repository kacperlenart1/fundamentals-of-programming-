# Program do zamiany wartości dwóch zmiennych przy użyciu zmiennej pomocniczej
x = 7
y = 34
z = 0  # dodatkowa, pomocnicza zmienna

print("Przed zamianą: x=", x, "y=", y)

# zamiana wartości zmiennych
s = x  # z przechowuje chwilowo wartość x (czyli 7)
x = y  # x otrzymuje wartość y (czyli 34)
y = s  # y otrzymuje dawną wartość x z zmiennej z (czyli 7)

print("Po zamianie: x=", x, "y=", y)