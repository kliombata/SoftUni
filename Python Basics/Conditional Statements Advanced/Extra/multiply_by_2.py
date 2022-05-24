number = 0

while number >= 0:
    number = float(input())
    if number >= 0:
        print(f"Result: {number * 2:.2f}")
    else:
        print("Negative number!")
