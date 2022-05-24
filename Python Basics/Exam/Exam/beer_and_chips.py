import math

fan_name = input()
budget = float(input())
num_beers = int(input())
num_chips = int(input())

price_per_beer = 1.20
cost_beers = num_beers * price_per_beer
price_per_chips = 0.45 * cost_beers
cost_chips = math.ceil(num_chips * price_per_chips)
total_cost = cost_beers + cost_chips
difference = abs(total_cost - budget)

if total_cost <= budget:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")
