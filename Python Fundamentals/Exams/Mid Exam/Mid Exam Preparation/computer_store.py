price = 0
taxes = 0
total_price = 0

while True:
    command = input()

    if command == "regular" or command == "special":
        break
    else:
        command = float(command)

    if command > 0:
        price += command
    else:
        print("Invalid price!")

total_price = price

if total_price == 0:
    print("Invalid order!")
else:
    taxes = 0.20 * price
    total_price += taxes

    if command == "special":
        total_price -= total_price * 0.10

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")