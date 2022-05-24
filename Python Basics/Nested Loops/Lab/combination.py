num = int(input())

valid_counter = 0
summary = 0

for i in range(0, num + 1):
    for j in range(0, num + 1):
        for k in range(0, num + 1):
            summary = i + j + k

            if summary == num:
                valid_counter += 1

print(valid_counter)
