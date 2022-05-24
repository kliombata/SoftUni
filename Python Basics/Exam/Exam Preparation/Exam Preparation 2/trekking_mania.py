num_groups = int(input())

total_counter = 0
musala_counter = 0
monblan_counter = 0
kilimanjaro_counter = 0
k2_counter = 0
everest_counter = 0

for groups in range(num_groups):
    current_group = int(input())
    total_counter += current_group

    if current_group <= 5:
        musala_counter += current_group
    elif current_group <= 12:
        monblan_counter += current_group
    elif current_group <= 25:
        kilimanjaro_counter += current_group
    elif current_group <= 40:
        k2_counter += current_group
    else:
        everest_counter += current_group

musala_percentage = (musala_counter / total_counter) * 100
monblan_percentage = (monblan_counter / total_counter) * 100
kilimanjaro_percentage = (kilimanjaro_counter / total_counter) * 100
k2_percentage = (k2_counter / total_counter) * 100
everest_percentage = (everest_counter / total_counter) * 100

print(f"{musala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
