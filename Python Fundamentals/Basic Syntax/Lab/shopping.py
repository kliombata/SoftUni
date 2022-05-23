budget = int(input())
command = input()

overdraft = False

while command != "End":
    current_input = int(command)
    budget -= current_input

    if budget < 0:
        overdraft = True
        break

    command = input()

if overdraft:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")