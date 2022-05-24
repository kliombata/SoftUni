width = int(input())
length = int(input())
height = int(input())

there_is_left_space = True
volume = width * length * height
command = input()

while command != "Done":
    num_boxes = int(command)
    volume -= num_boxes
    if volume <= 0:
        there_is_left_space = False
        break

    command = input()

if there_is_left_space:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
