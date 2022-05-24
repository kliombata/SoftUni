num_free_days = int(input())
days_in_year = 365
play_work_day = 63
play_free_day = 127
tom_norm = 30000

num_work_days = days_in_year - num_free_days
play_time = (num_free_days * play_free_day) + (num_work_days * play_work_day)
difference = abs(play_time - tom_norm)
hours = difference // 60
minutes = difference % 60

if play_time >= tom_norm:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
