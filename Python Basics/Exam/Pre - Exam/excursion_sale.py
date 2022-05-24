sea_excursions = int(input())
mountain_excursions = int(input())

money_counter = 0
command = input()
all_sea_excursions_sold = False
all_mountain_excursions_sold = False
all_excursions_sold = False

while command != "Stop":
    current_excursion = command

    if current_excursion == "sea":
        current_excursion = 680
        money_counter += current_excursion
        sea_excursions -= 1
        if all_sea_excursions_sold:
            money_counter -= current_excursion
    elif current_excursion == "mountain":
        current_excursion = 499
        money_counter += current_excursion
        mountain_excursions -= 1
        if all_mountain_excursions_sold:
            money_counter -= current_excursion

    if sea_excursions <= 0:
        all_sea_excursions_sold = True

    if mountain_excursions <= 0:
        all_mountain_excursions_sold = True

    if all_sea_excursions_sold and all_mountain_excursions_sold:
        all_excursions_sold = True
        break

    command = input()

if all_excursions_sold:
    print("Good job! Everything is sold.")

print(f"Profit: {money_counter} leva.")
