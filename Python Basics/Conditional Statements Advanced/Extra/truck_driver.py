season = input()
kilometers_per_month = float(input())

reward_per_month = 0

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        reward_per_month = kilometers_per_month * 0.75
    elif season == "Summer":
        reward_per_month = kilometers_per_month * 0.90
    elif season == "Winter":
        reward_per_month = kilometers_per_month * 1.05
elif kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        reward_per_month = kilometers_per_month * 0.95
    elif season == "Summer":
        reward_per_month = kilometers_per_month * 1.10
    elif season == "Winter":
        reward_per_month = kilometers_per_month * 1.25
else:
    reward_per_month = kilometers_per_month * 1.45

season_reward = reward_per_month * 4
season_reward = season_reward - (0.10 * season_reward)

print(f"{season_reward:.2f}")
