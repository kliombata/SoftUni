item = input()
quantity = int(input())


def calculations(item, quantity):
    price_per_item = 0

    if item == "coffee":
        price_per_item = 1.50
    elif item == "water":
        price_per_item = 1.00
    elif item == "coke":
        price_per_item = 1.40
    elif item == "snacks":
        price_per_item = 2.00


    final_price = price_per_item * quantity
    return  final_price

print(f"{calculations(item, quantity):.2f}")
