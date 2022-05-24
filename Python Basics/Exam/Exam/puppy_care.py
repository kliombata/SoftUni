bought_food_kg = int(input())

bought_food_gr = bought_food_kg * 1000
food_counter = 0
command = input()

while command != "Adopted":
    current_eating = int(command)
    food_counter += current_eating
    command = input()

difference = abs(food_counter - bought_food_gr)

if food_counter <= bought_food_gr:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
