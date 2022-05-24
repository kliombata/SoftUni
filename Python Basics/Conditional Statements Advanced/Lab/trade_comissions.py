city = input()
sales = float(input())

percentage = 0
is_valid = True

if city == "Sofia":
    if sales < 0:
        is_valid = False
    elif sales >= 0 and sales <= 500:
        percentage = 0.05
    elif sales > 500 and sales <= 1000:
        percentage = 0.07
    elif sales > 1000 and sales <= 10000:
        percentage = 0.08
    elif sales > 10000:
        percentage = 0.12
elif city == "Varna":
    if sales < 0:
        is_valid = False
    elif sales >= 0 and sales <= 500:
        percentage = 0.045
    elif sales > 500 and sales <= 1000:
        percentage = 0.075
    elif sales > 1000 and sales <= 10000:
        percentage = 0.10
    elif sales > 10000:
        percentage = 0.13
elif city == "Plovdiv":
    if sales < 0:
        is_valid = False
    elif sales >= 0 and sales <= 500:
        percentage = 0.055
    elif sales > 500 and sales <= 1000:
        percentage = 0.08
    elif sales > 1000 and sales <= 10000:
        percentage = 0.12
    elif sales > 10000:
        percentage = 0.145
else:
    is_valid = False

commission = sales * percentage

if is_valid:
    print(f"{commission:.2f}")
else:
    print("error")