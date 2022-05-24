import math

num_paint_buckets = int(input())
num_rolls = int(input())
price_per_gloves = float(input())
price_per_brush = float(input())

price_per_paint_bucket = 21.50
price_per_roll = 5.20
cost_paint_buckets = num_paint_buckets * price_per_paint_bucket
cost_rolls = num_rolls * price_per_roll
num_gloves = math.ceil(0.35 * num_rolls)
num_brushes = math.floor(0.48 * num_paint_buckets)
cost_gloves = num_gloves * price_per_gloves
cost_brushes = num_brushes * price_per_brush
total_cost = cost_paint_buckets + cost_rolls + cost_gloves + cost_brushes
delivery = (1/15) * total_cost

print(f"This delivery will cost {delivery:.2f} lv.")
