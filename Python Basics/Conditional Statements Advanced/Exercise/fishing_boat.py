budget = int(input())
season = input()
num_of_fishermen = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season == "Winter":
    rent = 2600
else:
    rent = 4200

if num_of_fishermen <= 6:
    rent = rent - (0.10 * rent)
elif num_of_fishermen <= 11:
    rent = rent - (0.15 * rent)
else:
    rent = rent - (0.25 * rent)

if num_of_fishermen % 2 == 0 and season != "Autumn":
    rent = rent - (0.05 * rent)

difference = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
