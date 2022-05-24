import math

num_magnolias = int(input())
num_hyacinths = int(input())
num_roses = int(input())
num_cacti = int(input())
gift = float(input())

price_per_magnolia = 3.25
price_per_hyacinth = 4
price_per_rose = 3.50
price_per_cactus = 8
# 5% taxes

magnolias = num_magnolias * price_per_magnolia
hyacinths = num_hyacinths * price_per_hyacinth
roses = num_roses * price_per_rose
cacti = num_cacti * price_per_cactus
net_total = magnolias + hyacinths + roses + cacti
total = net_total - (0.05 * net_total)
difference = abs(total - gift)

if total >= gift:
    difference = math.floor(difference)
    print(f"She is left with {difference} leva.")
else:
    difference = math.ceil(difference)
    print(f"She will have to borrow {difference} leva.")
