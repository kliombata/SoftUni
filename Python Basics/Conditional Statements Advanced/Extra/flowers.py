num_of_chrysanthemums = int(input())
num_of_roses = int(input())
num_of_tulips = int(input())
season = input()
holiday = input()

cost_per_chrysanthemum = 0
cost_per_rose = 0
cost_per_tulip = 0

if season == "Spring" or season == "Summer":
    cost_per_chrysanthemum = 2.00
    cost_per_rose = 4.10
    cost_per_tulip = 2.50
else:
    cost_per_chrysanthemum = 3.75
    cost_per_rose = 4.50
    cost_per_tulip = 4.15

num_flowers = num_of_chrysanthemums + num_of_roses + num_of_tulips
cost_flowers = (num_of_chrysanthemums * cost_per_chrysanthemum) + (num_of_roses * cost_per_rose) + (num_of_tulips * cost_per_tulip)

if holiday == "Y":
    cost_flowers = cost_flowers + (0.15 * cost_flowers)
else:
    pass

if num_of_tulips >= 7 and season == "Spring":
    cost_flowers = cost_flowers - (0.05 * cost_flowers)

if num_of_roses >= 10 and season == "Winter":
    cost_flowers = cost_flowers - (0.10 * cost_flowers)

if num_flowers >= 20:
    cost_flowers = cost_flowers - (0.20 * cost_flowers)

bouquet = cost_flowers + 2

print(f"{bouquet:.2f}")
