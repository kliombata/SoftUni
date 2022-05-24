first_number = int(input())
second_number = int(input())
operation = input()

result = 0
odd_or_even = "odd"

if operation == "+" or operation == "-" or operation == "*":
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    else:
        result = first_number * second_number
    if result % 2 == 0:
        odd_or_even = "even"
    print(f"{first_number} {operation} {second_number} = {result} - {odd_or_even}")
elif operation == "/" or operation == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        if operation == "/":
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result:.2f}")
        elif operation == "%":
            result = first_number % second_number
            print(f"{first_number} % {second_number} = {result}")
