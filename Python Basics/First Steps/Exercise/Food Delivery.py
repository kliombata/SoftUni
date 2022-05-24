num_chicken_menus = int(input())
num_fish_menus = int(input())
num_veg_menus = int(input())

chicken_menus = num_chicken_menus * 10.35
fish_menus = num_fish_menus * 12.40
veg_menus = num_veg_menus * 8.15
total_price = chicken_menus + fish_menus + veg_menus
dessert_price = total_price * 0.2
price = total_price + dessert_price + 2.5

print (price)