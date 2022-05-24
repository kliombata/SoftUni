deposit = float(input())
term = int(input())
interest = float(input())

#сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
conversion = interest / 100
amount_1 = deposit * conversion
amount_2 = amount_1 / 12
amount = deposit + term * amount_2

print (amount)