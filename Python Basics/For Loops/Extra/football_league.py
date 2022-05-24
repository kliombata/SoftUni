stadium_capacity = int(input())
fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
capacity = 0

for all_fans in range(fans):
    current_fan = input()

    if current_fan == "A":
        sector_a += 1
    elif current_fan == "B":
        sector_b += 1
    elif current_fan == "V":
        sector_v += 1
    elif current_fan == "G":
        sector_g += 1

sector_a = sector_a / fans * 100
sector_b = sector_b / fans * 100
sector_v = sector_v / fans * 100
sector_g = sector_g / fans * 100
capacity = fans / stadium_capacity * 100

print(f"{sector_a:.2f}%")
print(f"{sector_b:.2f}%")
print(f"{sector_v:.2f}%")
print(f"{sector_g:.2f}%")
print(f"{capacity:.2f}%")
