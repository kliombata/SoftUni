side_a = float(input())
side_b = float(input())

side_a *= 100
side_b *= 100
corridor = 100

rows = (side_b - corridor) // 70
collums = side_a // 120
total = int(rows + collums) - 3

print (total)