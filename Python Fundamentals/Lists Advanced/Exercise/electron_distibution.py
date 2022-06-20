electrons = int(input())

filled_shields = []
current_shield = 1
end = False

while end is not True:
    current_electrons = 2 * (current_shield ** 2)
    electrons -= current_electrons

    if electrons <= 0:
        electrons += current_electrons
        filled_shields.append(electrons)
        end = True
    else:
        filled_shields.append(current_electrons)

    current_shield += 1

print(filled_shields)
