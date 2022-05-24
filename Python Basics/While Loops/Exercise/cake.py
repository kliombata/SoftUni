width = int(input())
length = int(input())

total_cake_pieces = width * length
there_is_no_more_cake = False
command = input()

while command != "STOP":
    current_cake_pieces = int(command)
    total_cake_pieces -= current_cake_pieces
    if total_cake_pieces < 0:
        there_is_no_more_cake = True
        break

    command = input()

if there_is_no_more_cake:
    print(f"No more cake left! You need {abs(total_cake_pieces)} pieces more.")
else:
    print(f"{total_cake_pieces} pieces are left.")