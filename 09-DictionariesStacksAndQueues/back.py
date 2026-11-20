import queue

# Stos przechowujący historię odwiedzonych stron.
visited_websites = queue.LifoQueue()
for website in ("instagram.com", "uek.krakow.pl", "microsoft.com"):
    visited_websites.put(website)

current_website = "microsoft.com"

while True:
    website = input("Enter website name (0 for back): ").strip()

    if website == "0":
        if not visited_websites.empty():
            visited_websites.get()  # Usuwamy bieżącą stronę z historii.
        if visited_websites.empty():
            print("No previously visited website.")
            break
        current_website = visited_websites.get()  # Pobieramy poprzednią stronę.
        visited_websites.put(current_website)  # Zostawiamy ją jako bieżącą.
        print("<-- Going back to a previously visited website")
    elif website:
        current_website = website
        visited_websites.put(current_website)

    print("You are currently viewing:", current_website)
    print()
