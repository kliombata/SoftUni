num_groups = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
summary = 0

for groups in range(num_groups):
    current_group = int(input())

    summary += current_group

    if current_group <= 5:
        musala += current_group
    elif current_group <= 12:
        montblanc += current_group
    elif current_group <= 25:
        kilimanjaro += current_group
    elif current_group <= 40:
        k2 += current_group
    else:
        everest += current_group

musala = musala / summary * 100
montblanc = montblanc / summary * 100
kilimanjaro = kilimanjaro / summary * 100
k2 = k2 / summary * 100
everest = everest / summary * 100

print(f"{musala:.2f}%")
print(f"{montblanc:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")
