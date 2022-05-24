days = int(input())
type_of_room = input()
opinion = input()

nights = days - 1
price_per_night = 0

if type_of_room == "room for one person":
    price_per_night = 18
elif type_of_room == "apartment":
    price_per_night = 25
elif type_of_room == "president apartment":
    price_per_night = 35

cost = nights * price_per_night

if nights < 10:
    if type_of_room == "apartment":
        cost = cost - (0.30 * cost)
    elif type_of_room == "president apartment":
        cost = cost - (0.10 * cost)
elif nights >= 10 and nights< 15:
    if type_of_room == "apartment":
        cost = cost - (0.35 * cost)
    elif type_of_room == "president apartment":
        cost = cost - (0.15 * cost)
else:
    if type_of_room == "apartment":
        cost = cost - (0.50 * cost)
    elif type_of_room == "president apartment":
        cost = cost - (0.20 * cost)

if opinion == "positive":
    cost = cost + (0.25 * cost)
else:
    cost = cost - (0.10 * cost)

print(f"{cost:.2f}")
