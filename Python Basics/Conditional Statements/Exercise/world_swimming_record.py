world_record = float(input())
meters = float(input())
seconds_per_meter = float(input())

delay = (meters // 15) * 12.5
seconds = (meters * seconds_per_meter) + delay

if seconds < world_record:
    print(f" Yes, he succeeded! The new world record is {seconds:.2f} seconds.")
else:
    difference = (seconds - world_record)
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
