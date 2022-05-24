first_point_x = float(input())
first_point_y = float(input())
second_point_x = float(input())
second_point_y = float(input())
my_point_x = float(input())
my_point_y = float(input())

is_inside_or_outside = False

if my_point_x == first_point_x or my_point_x == second_point_x:
    if first_point_y <= my_point_y <= second_point_y:
        print("Border")
    else:
        print("Inside / Outside")
elif my_point_y == first_point_y or my_point_y == second_point_y:
    if first_point_x <= my_point_x <= second_point_x:
        print("Border")
    else:
        print("Inside / Outside")
else:
    print("Inside / Outside")

# if is_inside_or_outside:
#     print("Inside / Outside")
