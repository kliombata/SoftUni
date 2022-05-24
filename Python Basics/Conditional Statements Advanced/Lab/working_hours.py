time = int(input())
day = input()

is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"

if time >= 10 and time <= 18:
    if is_working_day:
        print("open")

if day == "Sunday" or time < 10 or time > 18:
    print("closed")
