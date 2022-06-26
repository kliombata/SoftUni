def shoot_func(targets):
    win_counter = 0

    while True:
        command = input()

        if command == "End":
            print(f"Shot targets {win_counter} -> {' '.join([str(x) for x in targets])}")
            break
        else:
            command = int(command)

        if command >= len(targets):
            continue
        else:
            current_value = targets[command]

            for current_target in targets:
                if current_target == current_value:
                    continue
                else:
                    if current_target == -1:
                        continue
                    elif current_target > current_value:
                        current_target -= current_value
                    elif current_target < current_value:
                        current_target += current_value

            targets[command] = -1
            win_counter += 1


data = list(map(int, input().split(" ")))
shoot_func(data)