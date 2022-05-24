count_of_numbers = int(input())

summary = 0
max_number = ""
difference = 0

for number in range(count_of_numbers):
    value = int(input())
    summary += value

    if number == 0:
        max_number = value

    if value > max_number:
        max_number = value

if max_number == summary - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (summary - max_number))
    print("No")
    print(f"Diff = {difference}")
