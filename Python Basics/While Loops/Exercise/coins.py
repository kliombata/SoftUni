change = float(input())

change = int(change * 100)
coins_counter = 0

coins_counter += change // 200
change = change % 200

coins_counter += change // 100
change = change % 100

coins_counter += change // 50
change = change % 50

coins_counter += change // 20
change = change % 20

coins_counter += change // 10
change = change % 10

coins_counter += change // 5
change = change % 5

coins_counter += change // 2
change = change % 2

coins_counter += change // 1
change = change % 1

print(coins_counter)
