n = int(input())

left_summary = 0

for i in range(n):
    value = int(input())
    left_summary += value

right_summary = 0

for i in range(n):
    value = int(input())
    right_summary += value

difference = abs(right_summary - left_summary)

if left_summary == right_summary:
    print(f"Yes, sum = {left_summary}")
else:
    print(f"No, diff = {difference}")
