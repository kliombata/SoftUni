fuel_type = input()  # "Gasoline" / "Diesel" / "Gas"
liters_fuel = float(input())
club_card = input()  # "Yes" / "No"

price_per_liter_gasoline = 2.22
price_per_liter_diesel = 2.33
price_per_liter_gas = 0.93
total = 0

if club_card == "Yes":
    price_per_liter_gasoline -= 0.18
    price_per_liter_diesel -= 0.12
    price_per_liter_gas -= 0.08
elif club_card == "No":
    pass

if fuel_type == "Gasoline":
    total = price_per_liter_gasoline * liters_fuel
elif fuel_type == "Diesel":
    total = price_per_liter_diesel * liters_fuel
elif fuel_type == "Gas":
    total = price_per_liter_gas * liters_fuel

if 20 <= liters_fuel <= 25:
    total = total - (0.08 * total)
elif liters_fuel > 25:
    total = total - (0.10 * total)

print(f"{total:.2f} lv.")
