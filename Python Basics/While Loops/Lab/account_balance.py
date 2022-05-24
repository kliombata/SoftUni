amount = input()

balance = 0

while amount != "NoMoreMoney":
    current_amount = float(amount)

    if current_amount < 0:
        print("Invalid operation!")
        break

    balance += current_amount
    print(f"Increase: {current_amount:.2f}")

    amount = input()

print(f"Total: {balance:.2f}")
