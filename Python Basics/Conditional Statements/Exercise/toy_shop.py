price_holiday = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

price_puzzle = 2.6
price_doll = 3
price_bear = 4.1
price_minion = 8.2
price_truck = 2

total_num = num_puzzles + num_dolls + num_bears + num_minions + num_trucks
reward = (num_puzzles * price_puzzle) + \
         (num_dolls * price_doll) + \
         (num_bears * price_bear) + \
         (num_minions * price_minion) + \
         (num_trucks * price_truck)
discount = 0

if total_num >= 50:
    discount = 0.25 * reward
    reward -= discount

rent = 0.10 * reward
final = reward - rent
difference = abs(final - price_holiday)

if final >= price_holiday:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
