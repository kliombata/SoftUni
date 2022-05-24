minutes_of_walking = int(input())
num_walking = int(input())
taken_calories = int(input())

total_minutes = minutes_of_walking * num_walking
calories_walking = total_minutes * 5
needed_calories = 0.50 * taken_calories

if calories_walking >= needed_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_walking}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_walking}.")
