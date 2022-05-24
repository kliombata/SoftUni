days = int(input())
available_food = float(input())

total_biscuits = 0
dog_counter = 0
cat_counter = 0
total_counter = 0

for period in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    dog_counter += dog_food
    cat_counter += cat_food
    total_counter += (dog_food + cat_food)

    if period % 3 == 0:
        total_biscuits += 0.10 * (dog_food + cat_food)

total_biscuits = round(total_biscuits)
total_percentage = (total_counter / available_food) * 100
dog_percentage = (dog_counter / total_counter) * 100
cat_percentage = (cat_counter / total_counter) * 100

print(f"Total eaten biscuits: {total_biscuits:.0f}gr.")
print(f"{total_percentage:.2f}% of the food has been eaten.")
print(f"{dog_percentage:.2f}% eaten from the dog.")
print(f"{cat_percentage:.2f}% eaten fro the cat.")
