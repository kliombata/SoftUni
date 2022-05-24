import sys

player_name = ""

hat_trick = False
most_goals = -sys.maxsize
best_player = ""

while True:
    player_name = input()
    if player_name == "END":
        break

    player_goals = int(input())

    if player_goals > most_goals:
        most_goals = player_goals
        best_player = player_name

    if 3 <= player_goals < 10:
        hat_trick = True
    elif player_goals >= 10:
        hat_trick = True
        break

print(f"{best_player} is the best player!")

if hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
