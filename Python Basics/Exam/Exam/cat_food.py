num_cats = int(input())

num_small_cats = 0
num_middle_cats = 0
num_big_cats = 0
cat_food_counter = 0

for all_cats in range(num_cats):
    current_cat = float(input())

    if 100 <= current_cat < 200:
        num_small_cats += 1
        cat_food_counter += current_cat
    elif 200 <= current_cat < 300:
        num_middle_cats += 1
        cat_food_counter += current_cat
    elif 300 <= current_cat < 400:
        num_big_cats += 1
        cat_food_counter += current_cat

cat_food_kg = cat_food_counter / 1000
cat_food_cost = cat_food_kg * 12.45

print(f"Group 1: {num_small_cats} cats.")
print(f"Group 2: {num_middle_cats} cats.")
print(f"Group 3: {num_big_cats} cats.")
print(f"Price for food per day: {cat_food_cost:.2f} lv.")
