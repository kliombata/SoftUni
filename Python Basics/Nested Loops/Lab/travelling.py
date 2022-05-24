destination = input()

budget = 0
deposit = 0

while destination != "End":
    budget = float(input())

    savings = 0
    while savings < budget:
        deposit = float(input())
        savings += deposit

    print(f"Going to {destination}!")

    destination = input()
