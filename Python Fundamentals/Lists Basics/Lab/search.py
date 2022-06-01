number = int(input())
keyword = input()

list = []
filtered_list = []

for i in range(number):
    current_string = input()
    list.append(current_string)

for string in list:
    if keyword in string:
        filtered_list.append(string)

print(list)
print(filtered_list)
