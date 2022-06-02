number = int(input())

capacity = 255
poured_liters_counter = 0

for i in range(number):
    current_liters = int(input())
    capacity -= current_liters
    poured_liters_counter += current_liters

    if capacity < 0:
        poured_liters_counter -= current_liters
        capacity += current_liters
        print("Insufficient capacity!")

print(poured_liters_counter)
