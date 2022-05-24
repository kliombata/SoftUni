start = input()
end = input()

for first_digit in range(int(start[0]), int(end[0]) + 1):
    if first_digit % 2 == 0:
        continue
    for second_digit in range(int(start[1]), int(end[1]) + 1):
        if second_digit % 2 == 0:
            continue
        for third_digit in range(int(start[2]), int(end[2]) + 1):
            if third_digit % 2 == 0:
                continue
            for fourth_digit in range(int(start[3]), int(end[3]) + 1):
                if fourth_digit % 2 == 0:
                    continue

                combination = int(f"{first_digit}{second_digit}{third_digit}{fourth_digit}")
                print(f"{combination}", end=" ")
