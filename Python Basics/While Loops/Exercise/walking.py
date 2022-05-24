goal = 10000
step_counter = 0
command = ""

while step_counter <= goal:
    command = input()

    if command == "Going home":
        current_step = int(input())
        step_counter += current_step
        break
    else:
        current_step = int(command)
        step_counter += current_step

difference = abs(step_counter - goal)
if step_counter >= goal:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
