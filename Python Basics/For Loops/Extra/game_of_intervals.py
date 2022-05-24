num_intervals = int(input())

range_one = 0
range_two = 0
range_three = 0
range_four = 0
range_five = 0
invalid_num = 0
result = 0

for intervals in range(num_intervals):
    current_interval = int(input())

    if 0 <= current_interval <= 9:
        result = result + (0.20 * current_interval)
        range_one += 1
    elif 10 <= current_interval <= 19:
        result = result + (0.30 * current_interval)
        range_two += 1
    elif 20 <= current_interval <= 29:
        result = result + (0.40 * current_interval)
        range_three += 1
    elif 30 <= current_interval <= 39:
        result = result + 50
        range_four += 1
    elif 40 <= current_interval <= 50:
        result = result + 100
        range_five += 1
    elif current_interval < 0 or current_interval > 50:
        result = result / 2
        invalid_num += 1

range_one = range_one / num_intervals * 100
range_two = range_two / num_intervals * 100
range_three = range_three / num_intervals * 100
range_four = range_four / num_intervals * 100
range_five = range_five / num_intervals * 100
invalid_num = invalid_num / num_intervals * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {range_one:.2f}%")
print(f"From 10 to 19: {range_two:.2f}%")
print(f"From 20 to 29: {range_three:.2f}%")
print(f"From 30 to 39: {range_four:.2f}%")
print(f"From 40 to 50: {range_five:.2f}%")
print(f"Invalid numbers: {invalid_num:.2f}%")
