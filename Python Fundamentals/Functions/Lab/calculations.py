operator = input()
first_number = int(input())
second_number = int(input())


def calculations(operator, a, b):
    result = None

    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number / second_number
    elif operator == "add":
        result = first_number + second_number
    else:
        result = first_number - second_number

    return result


print(int(calculations(operator, first_number, second_number)))
