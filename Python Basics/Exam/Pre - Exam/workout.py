import math

days = int(input())
kilometers = float(input())

goal = 1000
kilometers_counter = kilometers

for period in range(days):
    current_increase = int(input())
    current_increase_percentage = current_increase / 100
    kilometers = kilometers + (current_increase_percentage * kilometers)
    kilometers_counter += kilometers

difference = abs(kilometers_counter - goal)

if kilometers_counter >= goal:
    print(f"You've done a great job running {math.ceil(difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(difference)} more kilometers")
