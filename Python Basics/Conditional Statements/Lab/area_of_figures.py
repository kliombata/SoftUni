import math

print("Basic Area Of Figures Calculator")
print("--------------------------------")
figure = input("Input figure (square, rectangle, circle, triangle): ")

if figure == "square":
    side_a = float(input("Input side a: "))
    area = side_a ** 2
    print(f"{area: .3f}")
elif figure == "rectangle":
    side_a = float(input("Input side a: "))
    side_b = float(input("Input side b: "))
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input("Input radius: "))
    area = math.pi * (radius ** 2)
    print(f"{area:.3f}")
elif figure == "triangle":
    side_a = float(input("Input side a: "))
    height = float(input("Input height a: "))
    area = (height * side_a) / 2
    print(f"{area:.3f}")

print("--------------------------------")
