number = int(input())

for first_digit in range(number):
    for second_digit in range(number):
        for third_digit in range(number):
            print(f"{chr(97 + first_digit)}{chr(97 + second_digit)}{chr(97 + third_digit)}")
