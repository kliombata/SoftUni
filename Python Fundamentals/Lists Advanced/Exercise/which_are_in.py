first_list = input().split(", ")
second_list = input().split(", ")
final_list = []

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and not first_list in final_list:
            final_list.append(first_word)
            break

print(final_list)
