number = int(input())

positive_list = []
negative_list = []
positive_counter = 0
sum_negative = 0

for i in range(number):
    current_number = int(input())

    if current_number > 0:
        positive_counter += 1
        positive_list.append(current_number)
    else:
        negative_list.append(current_number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {sum(negative_list)}")
