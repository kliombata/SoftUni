first_num = int(input())
second_num = int(input())
magic_num = int(input())

counter = 0
summary = 0
flag = False

for i in range(first_num, second_num + 1):
    for j in range(first_num, second_num + 1):
        counter += 1
        summary = i + j

        if summary == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            flag = True
            break

    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_num}")
