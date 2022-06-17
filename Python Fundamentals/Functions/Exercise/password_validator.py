def valid_lenght(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        print("Password must be between 6 and 10 characters")
        return False

def valid_symbols(password):
    if password.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")
        return False


def valid_digits(password):
    digits_counter = 0

    for character in password:
        if character.isdigit():
            digits_counter += 1

    if digits_counter >= 2:
        return True
    else:
        print("Password must have at least 2 digits")
        return False


password = input()

valid_password = [valid_lenght(password), \
                  valid_symbols(password), \
                  valid_digits(password)]
if all(valid_password):
    print("Password is valid")
