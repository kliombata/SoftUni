import math

num_tournaments = int(input())
start_points = int(input())

current_points = start_points
num_won_tournaments = 0

for tournament in range(num_tournaments):
    current_tournament = input()

    if current_tournament == "W":
        current_points += 2000
        num_won_tournaments += 1
    elif current_tournament == "F":
        current_points += 1200
    elif current_tournament == "SF":
        current_points += 720

average_points = (current_points - start_points) / num_tournaments
average_points = math.floor(average_points)
win_percentage = (num_won_tournaments / num_tournaments) * 100

print(f"Final points: {current_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")
