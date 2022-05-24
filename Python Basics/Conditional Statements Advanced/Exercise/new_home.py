type_of_flower = input()  # Roses Dahlias Tulips Narcissus Gladiolus
num_of_flowers = int(input())
budget = int(input())

price_per_flower = 0

if type_of_flower == "Roses":
    price_per_flower = 5.00
elif type_of_flower == "Dahlias":
    price_per_flower = 3.80
elif type_of_flower == "Tulips":
    price_per_flower = 2.80
elif type_of_flower == "Narcissus":
    price_per_flower = 3.00
else:
    price_per_flower = 2.50

total = num_of_flowers * price_per_flower

if type_of_flower == "Roses" and num_of_flowers > 80:
    total = total - (0.10 * total)
elif type_of_flower == "Dahlias" and num_of_flowers > 90:
    total = total - (0.15 * total)
elif type_of_flower == "Tulips" and num_of_flowers > 80:
    total = total - (0.15 * total)
elif type_of_flower == "Narcissus" and num_of_flowers < 120:
    total = total + (0.15 * total)
elif type_of_flower == "Gladiolus" and num_of_flowers < 80:
    total = total + (0.20 * total)

difference = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {num_of_flowers} {type_of_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
