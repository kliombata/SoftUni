import math

num_days = int(input())
left_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_food = num_days * dog_food_per_day
cat_food = num_days * cat_food_per_day
turtle_food = (num_days * turtle_food_per_day) / 1000
needed_food = dog_food + cat_food + turtle_food
difference = abs(needed_food - left_food)

if needed_food <= left_food:
    extra_food = math.floor(difference)
    print(f"{extra_food} kilos of food left.")
else:
    less_food = math.ceil(difference)
    print(f"{less_food} more kilos of food are needed.")