### PLIK 1.16.py: Kompletny program sortujący dystanse rosnąco, temperatury malejąco i nazwy plików rosnąco z użyciem sorted().
distances_traveled = [120, 150, 180, 90, 200, 175, 160]  # Pokonane dystanse.
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]  # Dzienne temperatury.
file_names = [  # Lista nazw plików.
    "report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
    "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"
]  # Koniec listy nazw plików.

sorted_distances = sorted(distances_traveled)  # Sortujemy od najmniejszego do największego.
sorted_temperatures = sorted(daily_temperatures, reverse=True)  # Sortujemy od najwyższego do najniższego.
sorted_file_names = sorted(file_names)  # Sortujemy nazwy plików rosnąco.

print("Distances traveled (ascending):", sorted_distances)  # Wypisujemy posortowane dystanse.
print("Daily temperatures (descending):", sorted_temperatures)  # Wypisujemy posortowane temperatury.
print("File names (ascending):", sorted_file_names)  # Wypisujemy posortowane nazwy plików.
