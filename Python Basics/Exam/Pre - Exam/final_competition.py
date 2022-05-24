num_dancers = int(input())
points = float(input())
season = input()
destination = input()

money = 0

if destination == "Bulgaria":
    money = num_dancers * points
elif destination == "Abroad":
    money = (num_dancers * points) + (0.50 * (num_dancers * points))

cost_percentage = 0

if season == "winter":
    if destination == "Bulgaria":
        cost_percentage = 0.08
    elif destination == "Abroad":
        cost_percentage = 0.15
elif season == "summer":
    if destination == "Bulgaria":
        cost_percentage = 0.05
    elif destination == "Abroad":
        cost_percentage = 0.10

money = money - (cost_percentage * money)
charity_money = 0.75 * money
left_money = money - charity_money
money_per_dancer = left_money / num_dancers

print(f"Charity - {charity_money:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
