name = input()

years = 1
summary = 0
num_bad_grades = 0
graduated_student = True

while years <= 12:
    current_grade = float(input())

    if current_grade < 4:
        num_bad_grades += 1
        if num_bad_grades > 1:
            graduated_student = False
            print(f"{name} has been excluded at {years} grade")
            break
        continue

    summary += current_grade
    years += 1

average_grade = summary / 12

if graduated_student:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
