num_pages = int(input())
pages_per_hour = int(input())
num_days = int(input())

total_hours = num_pages / pages_per_hour
hours_per_day = total_hours / num_days
hours_per_day_1 = int(hours_per_day)

print (hours_per_day_1)