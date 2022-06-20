numbers_as_string = input().split(", ")
numbers = [int(number) for number in numbers_as_string]

print(f"Positive: {', '.join(str(number) for number in numbers if number >= 0)}")
print(f"Negative: {', '.join(str(number) for number in numbers if number < 0)}")
print(f"Even: {', '.join(str(number) for number in numbers if number % 2 == 0)}")
print(f"Odd: {', '.join(str(number) for number in numbers if number % 2 != 0)}")
