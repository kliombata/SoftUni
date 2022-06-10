list = (input()).split()
number = int(input())

final_list = []

for element in list:
    final_list.append(int(element))

for eliminations in range(number):
    final_list.remove(min(final_list))

final_list_to_string = ", ".join([str(element) for element in final_list])

print(final_list_to_string)
