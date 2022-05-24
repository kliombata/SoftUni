num_judges = int(input())

current_project = input()
total_summary = 0
project_counter = 0

while current_project != "Finish":
    summary = 0
    project_counter += 1

    for grades in range(num_judges):
        current_grade = float(input())
        summary += current_grade
        total_summary += current_grade

    current_project_average = summary / num_judges
    print(f"{current_project} - {current_project_average:.2f}.")

    current_project = input()

final_division = project_counter * num_judges
final_average = total_summary / final_division

print(f"Student's final assessment is {final_average:.2f}.")
