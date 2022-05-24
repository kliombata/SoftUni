budget = float(input())
statists = int(input())
outfits = float(input())

decor = budget * 0.1
price_outfits = statists * outfits

if statists > 150:
    price_outfits *= 0.9

needed_money = decor + price_outfits
difference = abs(needed_money - budget)

if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
