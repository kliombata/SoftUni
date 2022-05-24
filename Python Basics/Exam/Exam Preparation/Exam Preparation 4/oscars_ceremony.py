rent = int(input())

statues = rent - (0.30 * rent)
food = statues - (0.15 * statues)
sound = 0.5 * food

total = rent + food + statues + sound
print(f"{total:.2f}")
