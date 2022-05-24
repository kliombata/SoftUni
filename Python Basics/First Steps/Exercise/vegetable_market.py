price_per_kilo_vegetable = float(input())
price_per_kilo_fruit = float(input())
kilos_vegetables = int(input())
kilos_fruit = int(input())
euro = 1.94

sum_euro = (price_per_kilo_vegetable * kilos_vegetables +
            price_per_kilo_fruit * kilos_fruit) / euro

print (f'{sum_euro:.2f}')
