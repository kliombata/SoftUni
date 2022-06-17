workers = input().split()
happiness_factor = int(input())

workers = list(map(lambda x: int(x) * happiness_factor, workers))
filtered = list(filter(lambda x: x >= (sum(workers) / len(workers)), workers))

if len(filtered) >= len(workers) / 2:
    print(f"Score: {len(filtered)}/{len(workers)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(workers)}. Employees are not happy!")
