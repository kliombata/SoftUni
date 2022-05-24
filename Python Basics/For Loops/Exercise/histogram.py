count_of_numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(count_of_numbers):
    value = int(input())

    if value < 200:
        p1 += 1
    elif value < 400:
        p2 += 1
    elif value < 600:
        p3 += 1
    elif value < 800:
        p4 += 1
    else:
        p5 += 1

p1 = p1 / count_of_numbers * 100
p2 = p2 / count_of_numbers * 100
p3 = p3 / count_of_numbers * 100
p4 = p4 / count_of_numbers * 100
p5 = p5 / count_of_numbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
