num_students = int(input())

top_students = 0
great_students = 0
ok_students = 0
failed_students = 0
summary = 0

for students in range(num_students):
    current_student = float(input())

    summary += current_student

    if current_student <= 2.99:
        failed_students += 1
    elif current_student <= 3.99:
        ok_students += 1
    elif current_student <= 4.99:
        great_students += 1
    else:
        top_students += 1

top_students = top_students / num_students * 100
great_students = great_students / num_students * 100
ok_students = ok_students / num_students * 100
failed_students = failed_students / num_students * 100
average = summary / num_students

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {great_students:.2f}%")
print(f"Between 3.00 and 3.99: {ok_students:.2f}%")
print(f"Fail: {failed_students:.2f}%")
print(f"Average: {average:.2f}")
