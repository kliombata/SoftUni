budget = float(input())
season = input()

place = ""
destination = ""
cost = 0

if season == "summer":
    place = "Camp"
else:
    place = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        cost = 0.30 * budget
    else:
        cost = 0.70 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        cost = 0.40 * budget
    else:
        cost = 0.80 * budget
else:
    place = "Hotel"
    destination = "Europe"
    cost = 0.90 * budget

print(f"Somewhere in {destination}")
print(f"{place} - {cost:.2f}")
