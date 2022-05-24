num_bottles = int(input())

ml_per_bottle = 750
total_ml = ml_per_bottle * num_bottles

ml_per_plate = 5
num_plates = 0
ml_per_pot = 15
num_pots = 0

used_ml = 0
loops = 0
command = ""

while total_ml >= 0:
    command = input()

    if command == "End":
        break

    loops += 1
    num_dishes = int(command)

    if loops % 3 == 0:
        num_pots += num_dishes
        used_ml = num_dishes * ml_per_pot
        total_ml -= used_ml
    else:
        num_plates += num_dishes
        used_ml = num_dishes * ml_per_plate
        total_ml -= used_ml

if total_ml < 0:
    print(f"Not enough detergent, {abs(total_ml)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{num_plates} dishes and {num_pots} pots were washed.")
    print(f"Leftover detergent {total_ml} ml.")
