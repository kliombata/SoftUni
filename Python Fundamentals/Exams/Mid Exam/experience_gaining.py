needed_experience = float(input())
count_of_battles = int(input())

battle_counter = 0
gained_experience = 0
new_tank = False

for current_game in range(1, count_of_battles + 1):

    current_battle = float(input())

    if current_game % 15 == 0:
        current_battle += (0.05 * current_battle)
        gained_experience += current_battle
        battle_counter += 1
    elif current_game % 3 == 0:
        current_battle += (0.15 * current_battle)
        gained_experience += current_battle
        battle_counter += 1
    elif current_game % 5 == 0:
        current_battle -= (0.10 * current_battle)
        gained_experience += current_battle
        battle_counter += 1
    else:
        gained_experience += current_battle
        battle_counter += 1

    if gained_experience >= needed_experience:
        new_tank = True
        break

difference = abs(gained_experience - needed_experience)

if new_tank:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
