rent = float(input())

cake = 0.20 * rent
drinks = cake - (0.45 * cake)
entertainer = (1/3) * rent
total_cost = rent + cake + drinks + entertainer

print(total_cost)