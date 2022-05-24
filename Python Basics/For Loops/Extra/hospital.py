time_period = int(input())

num_doctors = 7
cured_patients = 0
ill_patients = 0

for days in range(1, time_period + 1):
    patients_current_day = int(input())

    if days % 3 == 0 and ill_patients > cured_patients:
        num_doctors += 1

    if patients_current_day <= num_doctors:
        cured_patients += patients_current_day
    else:
        ill_patients += patients_current_day - num_doctors
        cured_patients += num_doctors

print(f"Treated patients: {cured_patients}.")
print(f"Untreated patients: {ill_patients}.")
