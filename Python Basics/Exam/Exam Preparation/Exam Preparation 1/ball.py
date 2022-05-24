import math

num = int(input())

points = 0
red_balls_counter = 0
orange_balls_counter = 0
yellow_balls_counter = 0
white_balls_counter = 0
other_balls_counter = 0
black_balls_counter = 0

for i in range(num):
    current_ball = input()

    if current_ball == "red":
        points += 5
        red_balls_counter += 1
    elif current_ball == "orange":
        points += 10
        orange_balls_counter += 1
    elif current_ball == "yellow":
        points += 15
        yellow_balls_counter += 1
    elif current_ball == "white":
        points += 20
        white_balls_counter += 1
    elif current_ball == "black":
        points = math.floor(points / 2)
        black_balls_counter += 1
    else:
        other_balls_counter += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls_counter}")
print(f"Orange balls: {orange_balls_counter}")
print(f"Yellow balls: {yellow_balls_counter}")
print(f"White balls: {white_balls_counter}")
print(f"Other colors picked: {other_balls_counter}")
print(f"Divides from black balls: {black_balls_counter}")
