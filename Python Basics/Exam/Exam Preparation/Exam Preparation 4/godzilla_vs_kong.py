budget = float(input())
num_actors = int(input())
price_per_outfit = float(input())

decor = 0.10 * budget
outfits = num_actors * price_per_outfit

if num_actors >= 150:
    outfits = outfits - (0.10 * outfits)

total = decor + outfits
difference = abs(budget - total)

if total <= budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
