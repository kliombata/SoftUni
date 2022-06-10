factor = int(input())
count = int(input())

multiples_list = []

for multiplier in range(1, count + 1):
    multiples_list.append(factor * multiplier)

print(multiples_list)
