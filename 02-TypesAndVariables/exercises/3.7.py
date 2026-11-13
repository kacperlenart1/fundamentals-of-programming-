###
# Program obliczający i wyświetlający liczbę ludności 
# oraz procentowy udział ludności na półkuli północnej i południowej

total = 8000000000
north = 7200000000

# Obliczenie ludności na półkuli południowej
south = total - north

# Wyświetlenie wyników
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north / total * 100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south / total * 100)