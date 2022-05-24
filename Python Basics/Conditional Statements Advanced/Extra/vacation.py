budget = float(input())
season = input()

location = ""

if season == "Summer":
    location = "Alaska"
else:
    location = "Morocco"

type_of_accommodation = ""
cost = 0

if budget <= 1000:
    type_of_accommodation = "Camp"
    if season == "Summer":
        cost = 0.65 * budget
    else:
        cost = 0.45 * budget
elif budget <= 3000:
    type_of_accommodation = "Hut"
    if season == "Summer":
        cost = 0.80 * budget
    else:
        cost = 0.60 * budget
else:
    type_of_accommodation = "Hotel"
    cost = 0.90 * budget

print(f"{location} - {type_of_accommodation} - {cost:.2f}")
