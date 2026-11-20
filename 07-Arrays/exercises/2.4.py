### PLIK 2.4.py: Kompletny program wypisujący tygodniowy plan posiłków dla wszystkich dni od poniedziałku do niedzieli.
meal_plan = [  # Plan posiłków [Breakfast, Lunch, Dinner] na 7 dni.
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],  # Poniedziałek.
    ["Pancakes", "Sandwich", "Steak"],  # Wtorek.
    ["Smoothie", "Chicken Wrap", "Salmon"],  # Środa.
    ["Eggs", "Pasta", "Soup"],  # Czwartek.
    ["Toast", "Burrito", "Pizza"],  # Piątek.
    ["Cereal", "Salad", "Fish Tacos"],  # Sobota.
    ["Bagel", "Rice and Beans", "Stir-fry"]  # Niedziela.
]  # Koniec planu posiłków.


def weekday(n):  # Zwraca nazwę dnia tygodnia dla numeru n od 1 do 7.
    weekdays = [  # Lista dni tygodnia.
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]  # Koniec listy dni.
    return weekdays[n - 1]  # Zwracamy nazwę dnia.


def day_meal_plan(plan, day_number):  # Zwraca posiłki wybranego dnia oddzielone przecinkiem i spacją.
    return ", ".join(plan[day_number - 1])  # Łączymy posiłki w jeden napis.


print("WEEKLY MEAL PLAN")  # Nagłówek planu.
print("(Breakfast, Lunch, Dinner)")  # Opis kolejności posiłków.
print("==========================")  # Linia oddzielająca.
for day_number in range(1, 8):  # Przechodzimy przez wszystkie 7 dni tygodnia.
    print(f"{weekday(day_number)}: {day_meal_plan(meal_plan, day_number)}")  # Wypisujemy nazwę dnia oraz posiłki.
