deck_of_cards = input().split(", ")
shuffles = int(input())

for shuffle in range(shuffles):
    command = input().split(", ")

    if command[0] == "Add":
        if command[1] in deck_of_cards:
            print("Card is already in the deck")
        else:
            deck_of_cards.append(command[1])
            print("Card successfully added")
    elif command[0] == "Remove":
        if command[1] in deck_of_cards:
            deck_of_cards.remove(command[1])
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        index = int(command[1])
        if 0 <= index < len(deck_of_cards):
            deck_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command[0] == "Insert":
        index = int(command[1])
        if 0 <= index < len(deck_of_cards):
            if command[2] in deck_of_cards:
                print("Card is already added")
            else:
                deck_of_cards.insert(index, command[2])
                print("Card successfully added")
        else:
            print("Index out of range")

text = ", ".join(deck_of_cards)
print(text)