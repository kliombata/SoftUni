membership = int(input())

shoes = membership - (membership * 0.40)
outfit = shoes - (shoes * 0.20)
ball = outfit * 0.25
accessory = ball * 0.20
price = shoes + outfit + ball + accessory + membership

print (price)