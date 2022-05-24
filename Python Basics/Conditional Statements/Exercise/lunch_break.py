import math

show_name = input()
episode_duration = int(input())
lunch_break_duration = int(input())

lunch_duration = lunch_break_duration * (1/8)
rest_duration = lunch_break_duration * (1/4)
remainder = lunch_break_duration - (lunch_duration + rest_duration)
difference = math.ceil(abs(episode_duration - remainder))

if remainder >= episode_duration:
    print(f"You have enough time to watch {show_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {difference} more minutes.")
