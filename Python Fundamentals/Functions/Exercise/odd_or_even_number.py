def odd_or_even_sum(num):
    sum_even_numbers = 0
    sum_odd_numbers = 0

    for index in num:
        index_in_num = int(index)

        if index_in_num % 2 == 0:
            sum_even_numbers += index_in_num
        else:
            sum_odd_numbers += index_in_num

    return [sum_even_numbers, sum_odd_numbers]


number = int(input())
number_in_string = str(number)

sum_even_numbers = odd_or_even_sum(number_in_string)[0]
sum_odd_numbers = odd_or_even_sum(number_in_string)[1]

print(f"Odd sum = {sum_odd_numbers}, Even sum = {sum_even_numbers}")
