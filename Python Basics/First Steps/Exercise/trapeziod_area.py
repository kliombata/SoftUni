side_a = float(input())
side_b = float(input())
height = float(input())

new_height = height / 2
area = (side_a + side_b) * new_height
round(area)

print (f'{area:.2f}')