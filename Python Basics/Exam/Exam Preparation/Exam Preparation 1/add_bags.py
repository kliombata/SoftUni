price_above_20kg = float(input())
luggage_kg = float(input())
days_until_flying = int(input())
num_luggage = int(input())

luggage_price = 0

if luggage_kg < 10:
    luggage_price = 0.20 * price_above_20kg
elif 10 <= luggage_kg <= 20:
    luggage_price = 0.50 * price_above_20kg
else:
    luggage_price = price_above_20kg

if days_until_flying < 7:
    luggage_price = luggage_price + (0.40 * luggage_price)
elif 7 <= days_until_flying <= 30:
    luggage_price = luggage_price + (0.15 * luggage_price)
else:
    luggage_price = luggage_price + (0.10 * luggage_price)

luggage_price_total = luggage_price * num_luggage

print(f"The total price of bags is: {luggage_price_total:.2f} lv.")
