number_loads = int(input())

minibus = 0
price_per_ton_minibus = 200
tir = 0
price_per_ton_tir = 175
train = 0
price_per_ton_train = 120
summary = 0

for loads in range(number_loads):
    current_load = int(input())

    summary += current_load

    if current_load <= 3:
        minibus += current_load
    elif current_load <= 11:
        tir += current_load
    else:
        train += current_load

minibus_cost = minibus * price_per_ton_minibus
tir_cost = tir * price_per_ton_tir
train_cost = train * price_per_ton_train
total = minibus_cost + tir_cost + train_cost
average = total / summary

minibus_percentage = minibus / summary * 100
tir_percentage = tir / summary * 100
train_percentage = train / summary * 100

print(f"{average:.2f}")
print(f"{minibus_percentage:.2f}%")
print(f"{tir_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
