needed_money = float(input())
money = float(input())

spending_days = 0
all_days = 0
failed_saving = False

while money < needed_money:
    action = input()
    current_sum = float(input())
    all_days += 1

    if action == "save":
        money += current_sum
        spending_days = 0
    elif action == "spend":
        spending_days += 1
        money -= current_sum
        if money < 0:
            money = 0
        if spending_days == 5:
            failed_saving = True
            break

if failed_saving:
    print("You can't save the money.")
    print(f"{all_days}")
else:
    print(f"You saved the money for {all_days} days.")
