import math

group_size = int(input())
days = int(input())

coins_counter = 0

for i in range (1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5

    coins_counter += 50 - (2 * group_size)

    if i % 3 == 0:
        coins_counter -= (3 * group_size)
    if i % 5 == 0:
        coins_counter += (20 * group_size)
        if i % 3 == 0:
            coins_counter -= (2 * group_size)

coins_per_person = math.floor(coins_counter / group_size)
print(f"{group_size} companions received {coins_per_person} coins each.")
