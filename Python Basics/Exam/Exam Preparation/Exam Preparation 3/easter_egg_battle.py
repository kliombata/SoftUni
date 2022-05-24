first_player_eggs = int(input())
second_player_eggs = int(input())

first_player_lost = False
second_player_lost = False
command = input()

while command != "End of battle":
    if command == "one":
        second_player_eggs -= 1
    elif command == "two":
        first_player_eggs -= 1

    if first_player_eggs == 0:
        first_player_lost = True
        break
    elif second_player_eggs == 0:
        second_player_lost = True
        break

    command = input()

if first_player_lost:
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
elif second_player_lost:
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
else:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
