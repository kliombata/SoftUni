fail_max = int(input())

has_failed = False
failed_counter = 0
problem = input()
last_problem = ""
summary = 0
num_problems = 0

while problem != "Enough":
    score = float(input())
    summary += score
    num_problems += 1
    last_problem = problem

    if score <= 4:
        failed_counter += 1
        if failed_counter >= fail_max:
            has_failed = True
            break

    problem = input()

average = summary / num_problems
if not has_failed:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {num_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {fail_max} poor grades.")
