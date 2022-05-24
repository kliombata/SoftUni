import math

record = float(input())
meters = float(input())
seconds_per_meter = float(input())

time = meters * seconds_per_meter
friction = math.floor(meters / 50) * 30
total_time = time + friction
difference = abs(total_time - record)

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")
