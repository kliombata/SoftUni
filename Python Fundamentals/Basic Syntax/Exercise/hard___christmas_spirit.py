quantity = int(input())
days = int(input())

budget = 0
spirit = 0

ornament_set = 2
tree_skirt = 5
tree_gaarland = 3
tree_lights = 15

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        budget += ornament_set * quantity
        spirit += 5

    if current_day % 3 == 0:
        budget += (tree_skirt + tree_gaarland) * quantity
        spirit += 13

    if current_day % 5 == 0:
        budget += tree_lights * quantity
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30

    if current_day % 10 == 0:
        spirit -= 20
        budget += tree_skirt + tree_gaarland + tree_lights

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
