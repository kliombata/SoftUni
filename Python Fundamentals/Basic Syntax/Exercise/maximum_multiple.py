diviser = int(input())
boundary = int(input())

max_multiplier = 0

for current_number in range(boundary, diviser, -1):
    if current_number % diviser == 0:
        max_multiplier = current_number
        break

print(max_multiplier)