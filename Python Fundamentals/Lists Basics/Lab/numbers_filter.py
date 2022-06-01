number = int(input())

numbers = []
filtered_numbers = []
command_even = "even"
command_odd = "odd"
command_positive = "positive"
command_negative = "negative"

for i in range(number):
    current_number = int(input())
    numbers.append(current_number)

command = input()

for num in numbers:
    filter_command = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 != 0) or
        (command == command_positive and num >= 0) or
        (command == command_negative and num < 0)
    )

    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)
