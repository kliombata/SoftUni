num_of_juniors = int(input())
num_of_seniors = int(input())
type_of_route = input()

donation_per_junior = 0

if type_of_route == "trail":
    donation_per_junior = 5.50
elif type_of_route == "cross-country":
    donation_per_junior = 8.00
elif type_of_route == "downhill":
    donation_per_junior = 12.25
elif type_of_route == "road":
    donation_per_junior = 20.00

donation_per_senior = 0

if type_of_route == "trail":
    donation_per_senior = 7.00
elif type_of_route == "cross-country":
    donation_per_senior = 9.50
elif type_of_route == "downhill":
    donation_per_senior = 13.75
elif type_of_route == "road":
    donation_per_senior = 21.50

all_riders = num_of_juniors + num_of_seniors

if all_riders >= 50:
    if type_of_route == "cross-country":
        donation_per_junior = donation_per_junior - (0.25 * donation_per_junior)
        donation_per_senior = donation_per_senior - (0.25 * donation_per_senior)

total_donation = (num_of_seniors * donation_per_senior) + (num_of_juniors * donation_per_junior)
final = total_donation - (0.05 * total_donation)

print(f"{final:.2f}")
