month = input()
num_spent_hours = int(input())
num_people = int(input())
time = input()

price_per_hour = 0

if month == "march" or month == "april" or month == "may":
    if time == "day":
        price_per_hour = 10.50
    elif time == "night":
        price_per_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if time == "day":
        price_per_hour = 12.60
    elif time == "night":
        price_per_hour = 10.20

if num_people >= 4:
    price_per_hour = price_per_hour - (0.10 * price_per_hour)

if num_spent_hours >= 5:
    price_per_hour = price_per_hour - (0.50 * price_per_hour)

total_cost = num_people * num_spent_hours * price_per_hour

print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")
