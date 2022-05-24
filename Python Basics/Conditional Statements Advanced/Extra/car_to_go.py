budget = float(input())
season = input()

type_of_class = ""
type_of_car = ""
cost = 0

if budget <= 100:
    type_of_class = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        cost = 0.35 * budget
    elif season == "Winter":
        type_of_car = "Jeep"
        cost = 0.65 * budget
elif budget <= 500:
    type_of_class = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        cost = 0.45 * budget
    elif season == "Winter":
        type_of_car = "Jeep"
        cost = 0.80 * budget
else:
    type_of_class = "Luxury class"
    type_of_car = "Jeep"
    cost = 0.90 * budget

print(type_of_class)
print(f"{type_of_car} - {cost:.2f}")
