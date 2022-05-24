needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
work_hours = int(input())

paint_1 = needed_paint + (needed_paint * 0.1)
nylon_1 = needed_nylon + 2
nylon = nylon_1 * 1.50
paint = paint_1 * 14.50
thinner = needed_thinner * 5
price_materials = nylon + paint + thinner + 0.40
price_per_hour = price_materials * 0.3
price = price_materials + (work_hours * price_per_hour)
print (price)