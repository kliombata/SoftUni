kg_bought_food = int(input())

gr_brought_food = kg_bought_food * 1000
eaten_food_counter = 0
command = input()

while command != "Adopted":
    current_eaten_food = int(command)
    eaten_food_counter += current_eaten_food
    command = input()

difference = abs(eaten_food_counter - gr_brought_food)

if gr_brought_food >= eaten_food_counter:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
