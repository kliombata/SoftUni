price_strawberries = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_strawberries = float(input())

price_raspberries = price_strawberries / 2
price_oranges = price_raspberries - (0.40 * price_raspberries)
price_bananas = price_raspberries - (0.80 * price_raspberries)

strawberries = price_strawberries * kg_strawberries
raspberries = price_raspberries * kg_raspberries
oranges = price_oranges * kg_oranges
bananas = price_bananas * kg_bananas

total = strawberries + raspberries + oranges + bananas
print(f"{total:.2f}")
