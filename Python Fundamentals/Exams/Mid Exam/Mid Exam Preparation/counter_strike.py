energy = int(input())
won_battles_counter = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {won_battles_counter}. Energy left: {energy}")
        break

    distance = int(command)

    if energy >= distance:
        won_battles_counter += 1
        energy -= distance

        if won_battles_counter % 3 == 0:
            energy += won_battles_counter
    else:
        print(f"Not enough energy! Game ends with {won_battles_counter} won battles and {energy} energy")
        break
