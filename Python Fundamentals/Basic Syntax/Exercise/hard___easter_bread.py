budget = float(input())
price_flour = float(input())

price_eggs = 0.75 * price_flour
price_milk = (price_flour + (0.25 * price_flour)) / 4
price_loaf = price_flour + price_eggs + price_milk

loaf_count = 0
coloured_eggs = 0

while budget >= price_loaf:
    budget -= price_loaf
    loaf_count += 1
    coloured_eggs += 3

    if loaf_count % 3 == 0:
        coloured_eggs -= (loaf_count - 2)

print(f"You made {loaf_count} loaves of Easter bread! "
      f"Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")