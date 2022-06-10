list_of_events = input().split("|")
energy = 100
coins = 100

bakery_is_opened = True

for event in list_of_events:
    event_info = event.split("-")
    type_of_event = event_info[0]
    value_of_event = int(event_info[1])

    if type_of_event == "rest":
        temporary_energy = energy
        temporary_energy += value_of_event
        if temporary_energy > 100:
            temporary_energy = 100
        gained_energy = temporary_energy - energy
        print(f"You gained {gained_energy} energy.")
        energy = temporary_energy
        print(f"Current energy: {energy}.")
    elif type_of_event == "order":
        if energy >= 30:
            energy -= 30
            coins += value_of_event
            print(f"You earned {value_of_event} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
    else:
        if coins >= value_of_event:
            coins -= value_of_event
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            bakery_is_opened = False
            break

if bakery_is_opened:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
