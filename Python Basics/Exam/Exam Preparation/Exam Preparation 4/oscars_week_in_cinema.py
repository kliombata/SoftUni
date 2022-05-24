film_name = input()
category = input()
num_tickets = int(input())

price_per_ticket = 0

if category == "normal":
    if film_name == "A Star Is Born":
        price_per_ticket = 7.50
    elif film_name == "Bohemian Rhapsody":
        price_per_ticket = 7.35
    elif film_name == "Green Book":
        price_per_ticket = 8.15
    else:
        price_per_ticket = 8.75
elif category == "luxury":
    if film_name == "A Star Is Born":
        price_per_ticket = 10.50
    elif film_name == "Bohemian Rhapsody":
        price_per_ticket = 9.45
    elif film_name == "Green Book":
        price_per_ticket = 10.25
    else:
        price_per_ticket = 11.55
else:
    if film_name == "A Star Is Born":
        price_per_ticket = 13.50
    elif film_name == "Bohemian Rhapsody":
        price_per_ticket = 12.75
    elif film_name == "Green Book":
        price_per_ticket = 13.25
    else:
        price_per_ticket = 13.95

tickets = price_per_ticket * num_tickets

print(f"{film_name} -> {tickets:.2f} lv.")
