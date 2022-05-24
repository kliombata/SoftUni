num_people = int(input())
num_overnights = int(input())
num_transit_cards = int(input())
num_museum_tickets = int(input())

price_per_overnight = 20
price_per_transit_card = 1.60
price_per_museum_ticket = 6

overnights_per_person = price_per_overnight * num_overnights
transit_cards_per_person = price_per_transit_card * num_transit_cards
museum_tickets_per_person = price_per_museum_ticket * num_museum_tickets
total_per_person = overnights_per_person + transit_cards_per_person + museum_tickets_per_person
total_group = total_per_person * num_people
total_group = total_group + (0.25 * total_group)

print(f"{total_group:.2f}")
