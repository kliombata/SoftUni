season = input()
type_of_group = input()
num_kids = int(input())
num_overnights = int(input())

price_per_overnight = 0

if season == "Winter":
    if type_of_group == "boys" or type_of_group == "girls":
        price_per_overnight = 9.60
    elif type_of_group == "mixed":
        price_per_overnight = 10.00
elif season == "Spring":
    if type_of_group == "boys" or type_of_group == "girls":
        price_per_overnight = 7.20
    elif type_of_group == "mixed":
        price_per_overnight = 9.50
elif season == "Summer":
    if type_of_group == "boys" or type_of_group == "girls":
        price_per_overnight = 15
    elif type_of_group == "mixed":
        price_per_overnight = 20

cost_overnights = num_kids * num_overnights * price_per_overnight

if num_kids < 10:
    pass
elif num_kids >= 10 and num_kids < 20:
    cost_overnights = cost_overnights - (0.05 * cost_overnights)
elif num_kids < 50:
    cost_overnights = cost_overnights - (0.15 * cost_overnights)
else:
    cost_overnights = cost_overnights - (0.50 * cost_overnights)

sport = ""

if type_of_group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif type_of_group == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif type_of_group == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {cost_overnights:.2f} lv.")
