num_bitcoin = int(input())
num_yen = float(input())
commission = float(input())

bitcoin_to_leva = num_bitcoin * 1168
yen_to_dollars = num_yen * 0.15
dollars_to_leva = yen_to_dollars * 1.76
leva_to_euro = (bitcoin_to_leva + dollars_to_leva) / 1.95
percentage = commission / 100
final = leva_to_euro - (percentage * leva_to_euro)

print(f"{final:.2f}")
