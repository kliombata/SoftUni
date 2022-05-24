num_floors = int(input())
rooms_per_floor = int(input())

for floor in range(num_floors, 0, -1):
    for room in range(0, rooms_per_floor):

        if floor == num_floors:
            print(f"L{floor}{room}", end=" ")
        elif floor % 2 == 1:
            print(f"A{floor}{room}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")

    print()
