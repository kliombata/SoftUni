num_pairs = int(input())

previous_pair = int(input()) + int(input())
difference = 0

for pairs in range(num_pairs - 1):
    current_pair = int(input()) + int(input())

    if abs(previous_pair - current_pair) > difference:
        difference = abs(previous_pair - current_pair)

    previous_pair = current_pair

if difference == 0:
    print(f"Yes, value={previous_pair}")
else:
    print(f"No, maxdiff={difference}")
