money = float(input())
sex = input()
age = int(input())
sport = input()

membership_price = 0

if sex == "m":
    if sport == "Gym":
        membership_price = 42
    elif sport == "Boxing":
        membership_price = 41
    elif sport == "Yoga":
        membership_price = 45
    elif sport == "Zumba":
        membership_price = 34
    elif sport == "Dances":
        membership_price = 51
    elif sport == "Pilates":
        membership_price = 39
elif sex == "f":
    if sport == "Gym":
        membership_price = 35
    elif sport == "Boxing":
        membership_price = 37
    elif sport == "Yoga":
        membership_price = 42
    elif sport == "Zumba":
        membership_price = 31
    elif sport == "Dances":
        membership_price = 53
    elif sport == "Pilates":
        membership_price = 37

if age <= 19:
    membership_price = membership_price - (0.20 * membership_price)

difference = abs(money - membership_price)

if money >= membership_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")
