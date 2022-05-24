fuel_name = input()
liters_fuel = float(input())

needed_fuel = 25

if fuel_name == "Diesel":
    if liters_fuel < needed_fuel:
        print(f"Fill your tank with {fuel_name.lower()}!")
    else:
        print(f"You have enough {fuel_name.lower()}.")
elif fuel_name == "Gasoline":
    if liters_fuel < needed_fuel:
        print(f"Fill your tank with {fuel_name.lower()}!")
    else:
        print(f"You have enough {fuel_name.lower()}.")
elif fuel_name == "Gas":
    if liters_fuel < needed_fuel:
        print(f"Fill your tank with {fuel_name.lower()}!")
    else:
        print(f"You have enough {fuel_name.lower()}.")
else:
    print("Invalid fuel!")
