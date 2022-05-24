wanted_book = input()
book_is_found = False

current_book = input()
searched_books = 0

while current_book != "No More Books":
    if current_book == wanted_book:
        book_is_found = True
        break

    searched_books += 1
    current_book = input()

if book_is_found:
    print(f"You checked {searched_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {searched_books} books.")
