hours = int(input())
minutes = int(input())

hours *= 60
total_minutes = minutes + hours + 15
total_hours = total_minutes // 60
total_minutes = total_minutes % 60

if total_hours >= 24:
    total_hours = 0

print(f"{total_hours}:{total_minutes:02d}")
