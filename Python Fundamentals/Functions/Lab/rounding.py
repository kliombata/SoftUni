def rounding(numbers):
    new_list = []
    rounded_list = []

    for element in numbers:
        new_list.append(float(element))

    for element in new_list:
        rounded_number = round(element)
        rounded_list.append(rounded_number)

    return rounded_list


numbers = input().split()
print(rounding(numbers))
