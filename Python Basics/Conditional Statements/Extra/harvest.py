import math

field_area = int(input())
grape_per_square_meter = float(input())
needed_wine = int(input())
num_workers = int(input())

grape = grape_per_square_meter * field_area
wine = (0.40 * grape) / 2.5
difference = abs(wine - needed_wine)
wine_per_worker = difference / num_workers

if wine < needed_wine:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
