number = int(input())

for first_digit in range(1, 9 + 1):
    for second_digit in range(9, first_digit + 1, -1):
        for third_digit in range(0, 9 + 1):
            for fourth_digit in range(9, third_digit, -1):

                summary = first_digit + second_digit + third_digit + fourth_digit
                multiplication = first_digit * second_digit * third_digit * fourth_digit

                if summary == multiplication and number % 10 == 5:
                    combination = str(f"{first_digit}{second_digit}{third_digit}{fourth_digit}")
                    print(combination)
                    exit()

                if multiplication // summary == 3 and number % 3 == 0:
                    combination = str(f"{fourth_digit}{third_digit}{second_digit}{first_digit}")
                    print(combination)
                    exit()

print("Nothing found")
