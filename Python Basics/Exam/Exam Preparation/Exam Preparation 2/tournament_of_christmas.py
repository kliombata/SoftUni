days = int(input())

# command = input()
win_day_counter = 0
lose_day_counter = 0
total_charity = 0

for tournament in range(days):
    current_charity = 0
    win_counter = 0
    lose_counter = 0
    command = input()

    while command != "Finish":
        sport = command
        result = input()

        if result == "win":
            win_counter += 1
            current_charity += 20
        else:
            lose_counter += 1

        command = input()

    if win_counter > lose_counter:
        win_day_counter += 1
        current_charity = current_charity + (0.10 * current_charity)
    else:
        lose_day_counter += 1

    total_charity += current_charity


if win_day_counter > lose_day_counter:
    total_charity = total_charity + (0.20 * total_charity)
    won_tournament = True
else:
    won_tournament = False

if won_tournament:
    print(f"You won the tournament! Total raised money: {total_charity:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_charity:.2f}")
