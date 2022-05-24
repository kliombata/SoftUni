num_location = int(input())

for locations in range(num_location):
    expected_average = float(input())
    days = int(input())

    current_counter = 0

    for period in range(days):
        current_day = float(input())
        current_counter += current_day

    current_average = current_counter / days
    difference = abs(current_average - expected_average)

    if current_average >= expected_average:
        print(f"Good job! Average gold per day: {current_average:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")
