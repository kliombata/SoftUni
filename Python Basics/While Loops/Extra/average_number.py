loops = int(input())
summary = 0

for n in range(loops):
    current_number = int(input())
    summary += current_number

average = summary / loops
print(f"{average:.2f}")
