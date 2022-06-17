def palidrome_numbers(numbers):
    for current_number in numbers:
        if current_number == current_number[::-1]:
            print("True")
        else:
            print("False")


input_list = input().split(", ")
palidrome_numbers(input_list)
