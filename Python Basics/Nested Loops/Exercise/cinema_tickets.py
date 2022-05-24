command = input()

students_tickets_counter = 0
standard_tickets_counter = 0
kids_tickets_counter = 0
total_tickets_sold = 0

while command != "Finish":
    movie_name = command
    total_places = int(input())
    sold_tickets = 0

    while sold_tickets != total_places:
        current_ticket = input()

        if current_ticket == "End":
            break
        elif current_ticket == "student":
            students_tickets_counter += 1
        elif current_ticket == "standard":
            standard_tickets_counter += 1
        elif current_ticket == "kid":
            kids_tickets_counter += 1

        sold_tickets += 1
        total_tickets_sold += 1

    current_film_capacity = (sold_tickets / total_places) * 100
    print(f"{movie_name} - {current_film_capacity:.2f}% full.")

    command = input()

student_percentage = (students_tickets_counter / total_tickets_sold) * 100
standard_percentage = (standard_tickets_counter / total_tickets_sold) * 100
kids_percentage = (kids_tickets_counter / total_tickets_sold) * 100

print(f"Total tickets: {total_tickets_sold}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")
