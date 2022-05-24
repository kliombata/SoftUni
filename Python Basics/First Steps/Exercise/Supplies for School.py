num_pens = int(input())
num_markers = int(input())
liters_detergent = int(input())
interest_percentage = int(input())

interest = interest_percentage / 100
pens = num_pens * 5.80
markers = num_markers * 7.20
detergent = liters_detergent * 1.20
total_price = pens + markers + detergent
price = total_price - (total_price * interest)

print (price)