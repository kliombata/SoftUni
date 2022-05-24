flavor = input()
size = input()
num_packages = int(input())

price_per_booster = 0
boosters_per_package = 0
total_price = 0

if size == "small":
    boosters_per_package = 2
    if flavor == "Watermelon":
        price_per_booster = 56
    elif flavor == "Mango":
        price_per_booster = 36.66
    elif flavor == "Pineapple":
        price_per_booster = 42.10
    elif flavor == "Raspberry":
        price_per_booster = 20
elif size == "big":
    boosters_per_package = 5
    if flavor == "Watermelon":
        price_per_booster = 28.70
    elif flavor == "Mango":
        price_per_booster = 19.60
    elif flavor == "Pineapple":
        price_per_booster = 24.80
    elif flavor == "Raspberry":
        price_per_booster = 15.20

total_price = (boosters_per_package * price_per_booster) * num_packages

if 400 <= total_price <= 1000:
    total_price = total_price - (0.15 * total_price)
elif total_price > 1000:
    total_price = total_price - (0.50 * total_price)

print(f"{total_price:.2f} lv.")
