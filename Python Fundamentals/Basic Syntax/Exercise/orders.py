num_orders = int(input())

total_price = 0

for order in range(num_orders):
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day > 2000:
        continue

    price = capsule_price * days * capsule_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
