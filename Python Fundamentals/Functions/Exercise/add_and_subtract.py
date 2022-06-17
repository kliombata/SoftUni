def sum_numbers(a, b):
    sumary = a + b
    return sumary


def subtract(sum, c):
    subtraction = sum - c
    return subtraction


def add_and_subtract(a, b, c):
    sum_a_and_b = sum_numbers(a, b)
    result = subtract(sum_a_and_b, c)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
