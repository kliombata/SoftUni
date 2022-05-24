age = int(input())
price_washing_machine = float(input())
price_per_toy = int(input())

total_money = 0
total_toys = 0
birthday_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 != 0:
        total_toys += 1
    elif birthday % 2 == 0:
        birthday_money += 10
        total_money += birthday_money - 1

total_money += (total_toys * price_per_toy)
difference = abs(total_money - price_washing_machine)

if total_money >= price_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
