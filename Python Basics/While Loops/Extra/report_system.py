needed_money = int(input())

gathered_money = 0
loops = 1
money_cs = 0
loops_cs = 0
money_cc = 0
loops_cc = 0
failed_charity = False
command = ""

while gathered_money <= needed_money:
    command = input()

    if command == "End":
        print("Failed to collect required money for charity.")
        failed_charity = True
        break

    loops += 1
    current_money = int(command)

    if loops % 2 == 0:
        if current_money > 100:
            print("Error in transaction!")
            continue
        gathered_money += current_money
        money_cs += current_money
        loops_cs += 1
        print("Product sold!")
    elif loops % 2 == 1:
        if current_money < 10:
            print("Error in transaction!")
            continue
        gathered_money += current_money
        money_cc += current_money
        loops_cc += 1
        print("Product sold!")

average_cs = money_cs / loops_cs
average_cc = money_cc / loops_cc

if not failed_charity:
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
