free_space = float(input())

suitcases_counter = 0
overloaded_plane = False
command = input()

while command != "End":
    current_suitcase = float(command)
    suitcases_counter += 1

    if suitcases_counter % 3 == 0:
        current_suitcase = current_suitcase + (0.10 * current_suitcase)

    free_space -= current_suitcase

    if free_space < 0:
        suitcases_counter -= 1
        overloaded_plane = True
        break

    command = input()

if overloaded_plane:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases_counter} suitcases loaded.")
