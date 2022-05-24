text = input()

summary = 0

for letter in text:
    if letter == "a":
        summary += 1
    elif letter == "e":
        summary += 2
    elif letter == "i":
        summary += 3
    elif letter == "o":
        summary += 4
    elif letter == "u":
        summary += 5

print(summary)
