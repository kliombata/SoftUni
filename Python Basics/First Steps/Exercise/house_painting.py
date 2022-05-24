side_a = float(input())
side_b = float(input())
height = float(input())

#Литър за квадратен метър боя (зелена/червена)
liter_per_square_meter_green = 3.4
liter_per_square_meter_red = 4.3

#Размери на препятствия в метри
door = 1.2 * 2
window = 1.5 * 1.5

#Пресмятане на нужните литри зелена боя
front_and_back = (side_a * side_a * 2) - door
sides = (side_a * side_b * 2) - (2 * window)
green_paint = (front_and_back + sides) / liter_per_square_meter_green

#Пресмятане на нужноте литри червена боя
roof_front_and_back = ((side_a * height) / 2) * 2
roof_sides = (side_a * side_b) * 2
red_paint = (roof_front_and_back + roof_sides) / liter_per_square_meter_red

print (f'{green_paint:.2f}')
print (f'{red_paint:.2f}')