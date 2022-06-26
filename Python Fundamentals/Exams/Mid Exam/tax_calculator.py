vechiles = [str(x) for x in input().split(">>")]

tax_per_year = 0
collected_taxes = 0

for current_car in vechiles:
    current_vechicle = current_car.split(" ")
    car_type = current_vechicle[0]
    years = int(current_vechicle[1])
    kilometers = int(current_vechicle[2])
    tax_current_vechicle = 0

    if car_type == "family":
        tax_per_year = 50
        tax_current_vechicle = ((kilometers // 3000) * 12) + (tax_per_year - (years * 5))
        collected_taxes += tax_current_vechicle
        print(f"A {car_type} car will pay {tax_current_vechicle:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        tax_per_year = 80
        tax_current_vechicle = ((kilometers // 9000) * 14) + (tax_per_year - (years * 8))
        collected_taxes += tax_current_vechicle
        print(f"A {car_type} car will pay {tax_current_vechicle:.2f} euros in taxes.")
    elif car_type == "sports":
        tax_per_year = 100
        tax_current_vechicle = ((kilometers // 2000) * 18) + (tax_per_year - (years * 9))
        collected_taxes += tax_current_vechicle
        print(f"A {car_type} car will pay {tax_current_vechicle:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {collected_taxes:.2f} euros in taxes.")
