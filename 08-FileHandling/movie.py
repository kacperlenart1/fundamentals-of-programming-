from pathlib import Path

# Dane filmu
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Plik wynikowy zapisujemy obok tego skryptu.
file_name = Path(__file__).resolve().parent / "movie_details.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name.name}.")
