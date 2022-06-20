version = list(map(int, input().split(".")))

version[-1] += 1
for current_index in range(len(version) - 1, -1, -1):
    if version[current_index] > 9:
        version[current_index] = 0
        version[current_index - 1] += 1

print(".".join(str(number) for number in version))
