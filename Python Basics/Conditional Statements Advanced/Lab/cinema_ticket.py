day = input()

is_12_leva = day == "Monday" or day == "Tuesday" or day == "Friday"
is_16_leva = day == "Saturday" or day == "Sunday"

if is_12_leva:
    print("12")
elif is_16_leva:
    print("16")
else:
    print("14")
