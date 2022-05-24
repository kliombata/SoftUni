budget = float(input())
overnights = int(input())
price_per_overnight = float(input())
others_percentage = int(input())

discount = 0

if overnights > 7:
    discount = 0.05
    price_per_overnight = price_per_overnight - (discount * price_per_overnight)

price_hotel = overnights * price_per_overnight
price_others = (others_percentage / 100) * budget
total = price_others + price_hotel
difference = abs(budget - total)

if budget >= total:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
