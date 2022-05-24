num_joinery = int(input())
type_of_joinery = input()
delivery = input()

price_joinery = 0
price_per_joiner = 0

if num_joinery < 10:
    print("Invalid order")
elif type_of_joinery == "90X130":
    price_per_joinery = 110
    price_joinery = price_per_joinery * num_joinery
    if 30 <= num_joinery < 60:
        price_joinery = price_joinery - (0.05 * price_joinery)
    elif num_joinery >= 60:
        price_joinery = price_joinery - (0.08 * price_joinery)

    if delivery == "With delivery":
        price_joinery += 60
    if num_joinery > 99:
        price_joinery = price_joinery - (0.04 * price_joinery)
    print(f"{price_joinery:.2f} BGN")

elif type_of_joinery == "100X150":
    price_per_joinery = 140
    price_joinery = price_per_joinery * num_joinery
    if 40 <= num_joinery < 80:
        price_joinery = price_joinery - (0.06 * price_joinery)
    elif num_joinery >= 80:
        price_joinery = price_joinery - (0.10 * price_joinery)

    if delivery == "With delivery":
        price_joinery += 60
    if num_joinery > 99:
        price_joinery = price_joinery - (0.04 * price_joinery)
    print(f"{price_joinery:.2f} BGN")

elif type_of_joinery == "130X180":
    price_per_joinery = 190
    price_joinery = price_per_joinery * num_joinery
    if 20 <= num_joinery < 50:
        price_joinery = price_joinery - (0.07 * price_joinery)
    elif num_joinery >= 50:
        price_joinery = price_joinery - (0.12 * price_joinery)

    if delivery == "With delivery":
        price_joinery += 60
    if num_joinery > 99:
        price_joinery = price_joinery - (0.04 * price_joinery)
    print(f"{price_joinery:.2f} BGN")

elif type_of_joinery == "200X300":
    price_per_joinery = 250
    price_joinery = price_per_joinery * num_joinery
    if 25 <= num_joinery < 50:
        price_joinery = price_joinery - (0.09 * price_joinery)
    elif num_joinery >= 50:
        price_joinery = price_joinery - (0.14 * price_joinery)

    if delivery == "With delivery":
        price_joinery += 60
    if num_joinery > 99:
        price_joinery = price_joinery - (0.04 * price_joinery)
    print(f"{price_joinery:.2f} BGN")
