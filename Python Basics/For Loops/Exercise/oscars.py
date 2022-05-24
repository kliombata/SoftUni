name_actor = input()
points_academy = float(input())
num_jury = int(input())

final_points = 0

for current_grade in range(num_jury):
    current_name = input()
    current_points = float(input())

    final_points = (len(current_name) * current_points) / 2
    points_academy += final_points

    if points_academy > 1250.5:
        break

difference = abs(points_academy - 1250.5)

if points_academy > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_academy:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {difference:.1f} more!")
