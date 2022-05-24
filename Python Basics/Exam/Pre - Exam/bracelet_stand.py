pocket_money_per_day = float(input())
revenue_per_day = float(input())
total_cost = float(input())
gift_price = float(input())

days = 5
total_pocket_money = days * pocket_money_per_day
total_revenue = days * revenue_per_day
total_money = (total_pocket_money + total_revenue) - total_cost
difference = abs(total_money - gift_price)

if total_money >= gift_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {difference:.2f} BGN.")
