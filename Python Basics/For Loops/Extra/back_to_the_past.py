inherited_money = float(input())
end_year = int(input())

budget = inherited_money
age = 18

for year in range(1800, end_year + 1):

    if year >= 1801:
        age += 1

    if year % 2 == 0:
        budget -= 12000
    else:
        budget -= 12000 + (50 * age)

if budget <= inherited_money and budget < 0:
    print(f"He will need {abs(budget):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {budget:.2f} dollars left.")

