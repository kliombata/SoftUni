kilometers = int(input())
time = input()

taxi_start = 0.70
taxi_kilometer_day = 0.79
taxi_kilometer_night = 0.90
bus_kilometer = 0.09  # At least 20 kilometers
train_kilometer = 0.06  # At least 100 kilometers
price = 0

if time == "day":
    taxi = kilometers * taxi_kilometer_day + 0.70
else:
    taxi = kilometers * taxi_kilometer_night + 0.70

if kilometers < 20:
    price = taxi  # Taxi
elif kilometers < 100:
    price = kilometers * bus_kilometer  # Bus
else:
    price = kilometers * train_kilometer  # Train

print(f"{price:.2f}")
