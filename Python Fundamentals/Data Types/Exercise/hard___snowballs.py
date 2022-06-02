number_of_snowballs = int(input())

highest_value = 0
best_weight = 0
best_time = 0
best_quality = 0


for current_snowball in range(number_of_snowballs):
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = int((current_snowball_weight / current_snowball_time) ** current_snowball_quality)

    if current_snowball_value > highest_value:
        highest_value = current_snowball_value

    if highest_value == current_snowball_value:
        best_weight = current_snowball_weight
        best_time = current_snowball_time
        best_quality = current_snowball_quality

print(f"{best_weight} : {best_time} = {highest_value} ({best_quality})")
