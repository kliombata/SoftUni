offers_list_as_strings = input().split(", ")
num_of_beggars = int(input())

final_list = []
index_counter = 0
offers_list = []

for element in offers_list_as_strings:
    offers_list.append(int(element))

while index_counter < num_of_beggars:
    current_beggar = 0

    for current_index in range(index_counter, len(offers_list), num_of_beggars):
        current_beggar += offers_list[current_index]

    index_counter += 1
    final_list.append(current_beggar)

print(final_list)
