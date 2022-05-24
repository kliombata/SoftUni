animal = input()

is_reptile = animal == "crocodile" or animal == "tortoise" or animal == "snake"

if is_reptile:
    print("reptile")
elif animal == "dog":
    print("mammal")
else:
    print("unknown")
