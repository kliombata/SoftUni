lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())

expenses_counter = 0
trashed_shields_counter = 0

for current_lost in range(1, lost_fights + 1):
    if current_lost % 2 == 0:
        expenses_counter += price_helmet
    if current_lost % 3 == 0:
        expenses_counter += price_sword
    if current_lost % 2 == 0 and current_lost % 3 == 0:
        expenses_counter += price_shield
        trashed_shields_counter += 1
    if trashed_shields_counter % 2 == 0 and trashed_shields_counter != 0:
        expenses_counter += price_armor
        trashed_shields_counter = 0

print(f"Gladiator expenses: {expenses_counter:.2f} aureus")
