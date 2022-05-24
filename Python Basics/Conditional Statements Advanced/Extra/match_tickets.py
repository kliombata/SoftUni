budget = float(input())
type_of_ticket = input()
num_of_fans = int(input())

ticket_price = 0

if type_of_ticket == "VIP":
    ticket_price = 499.99
elif type_of_ticket == "Normal":
    ticket_price = 249.99

transport_cost = 0

if num_of_fans <= 4:
    transport_cost = 0.75 * budget
elif num_of_fans <= 9:
    transport_cost = 0.60 * budget
elif num_of_fans <= 24:
    transport_cost = 0.50 * budget
elif num_of_fans <= 49:
    transport_cost = 0.40 * budget
else:
    transport_cost = 0.25 * budget

ticket_cost = num_of_fans * ticket_price
total_cost = ticket_cost + transport_cost
difference = abs(total_cost - budget)

if total_cost <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
