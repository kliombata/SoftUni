command = input()

double_letter = ""
new_text = ""

while command != "End":

    if command == "SoftUni":
        command = input()
        continue

    for index, letter in enumerate(command):
        double_letter = letter * 2
        new_text += double_letter

    print(new_text)
    double_letter = ""
    new_text = ""

    command = input()