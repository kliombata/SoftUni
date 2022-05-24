month = input()
nights = int(input())

type_one = "studio"
type_two = "apartment"

price_per_night_studio = 0
price_per_night_apartment = 0

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apartment = 65
elif month == "June" or month == "September":
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
else:
    price_per_night_studio = 76
    price_per_night_apartment = 77

if type_one == "studio" and (month == "May" or month == "October"):
    if nights > 7 and nights <= 14:
        price_per_night_studio = price_per_night_studio - (0.05 * price_per_night_studio)
    elif nights > 14:
        price_per_night_studio = price_per_night_studio - (0.30 * price_per_night_studio)
elif type_one == "studio" and (month == "June" or month == "September") and nights > 14:
    price_per_night_studio = price_per_night_studio - (0.20 * price_per_night_studio)

if type_two == "apartment" and nights > 14:
    price_per_night_apartment = price_per_night_apartment - (0.10 * price_per_night_apartment)

cost_studio = nights * price_per_night_studio
cost_apartment = nights * price_per_night_apartment

print(f"Apartment: {cost_apartment:.2f} lv.")
print(f"Studio: {cost_studio:.2f} lv.")
