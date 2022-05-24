n = int(input())

even_summary = 0
odd_summary = 0

for i in range(1, n + 1):
    value = int(input())

    if i % 2 == 0:
        even_summary += value
    else:
        odd_summary += value

difference = abs(even_summary - odd_summary)

if even_summary == odd_summary:
    print("Yes")
    print(f"Sum = {even_summary}")
else:
    print("No")
    print(f"Diff = {difference}")
