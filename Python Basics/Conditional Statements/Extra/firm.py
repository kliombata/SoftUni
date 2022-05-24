import math

needed_hours = int(input())
working_days_available = int(input())
extra_workers = int(input())

working_hours_per_day = 8
extra_working_hours_per_day = 2

seminars = 0.1 * working_days_available
actual_work = (working_days_available - seminars) * working_hours_per_day
extra_work = extra_workers * (working_days_available * extra_working_hours_per_day)
total = math.floor(actual_work + extra_work)
difference = abs(total - needed_hours)

if total >= needed_hours:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")
