agency_name = input()
num_adult_tickets = int(input())
num_kid_tickets = int(input())
net_price_adult_ticket = float(input())
service_fee = float(input())

net_price_kid_ticket = net_price_adult_ticket - (0.70 * net_price_adult_ticket)
profit_per_adult_ticket = net_price_adult_ticket + service_fee
profit_per_kid_ticket = net_price_kid_ticket + service_fee
profit_adult_tickets = num_adult_tickets * profit_per_adult_ticket
profit_kid_tickets = num_kid_tickets * profit_per_kid_ticket
profit_all = profit_kid_tickets + profit_adult_tickets
final_profit = 0.20 * profit_all

print(f"The profit of your agency from {agency_name} tickets is {final_profit:.2f} lv.")
