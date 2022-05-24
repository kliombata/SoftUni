days = int(input())
all_food = float(input())

dog_counter = 0
cat_counter = 0
total_counter = 0
biscuits_counter = 0

for current_day in range(1, days + 1):
    current_food_dog = int(input())
    current_food_cat = int(input())

    dog_counter += current_food_dog
    cat_counter += current_food_cat
    total_counter += (current_food_cat + current_food_dog)

    if current_day % 3 == 0:
        biscuits_counter += (0.10 * (current_food_cat + current_food_dog))

biscuits_counter = round(biscuits_counter)
total_percentage = (total_counter / all_food) * 100
dog_percentage = (dog_counter / total_counter) * 100
cat_percentage = (cat_counter / total_counter) * 100

print(f"Total eaten biscuits: {biscuits_counter:.0f}gr.")
print(f"{total_percentage:.2f}% of the food has been eaten.")
print(f"{dog_percentage:.2f}% eaten from the dog.")
print(f"{cat_percentage:.2f}% eaten from the cat.")
