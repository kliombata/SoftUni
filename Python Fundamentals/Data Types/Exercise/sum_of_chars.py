number = int(input())

sum_ascii = 0

for i in range(number):
    current_char = input()
    sum_ascii += ord(current_char)

print(f"The sum equals: {sum_ascii}")
