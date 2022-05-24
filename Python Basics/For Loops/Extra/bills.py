num_months = int(input())

electricity = 0
sum_electricity = 0
water = 20
internet = 15
others = 0
sum_others = 0

for months in range(num_months):
    current_month = float(input())

    sum_electricity += current_month

    others = (current_month + water + internet) + (0.20 * (current_month + water +internet))
    sum_others += others

sum_water = water * num_months
sum_internet = internet * num_months
average = (sum_electricity + sum_water + sum_internet + sum_others) / num_months

print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {sum_others:.2f} lv")
print(f"Average: {average:.2f} lv")
