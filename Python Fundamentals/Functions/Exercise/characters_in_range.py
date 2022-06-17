def chatacters_in_range(first, second):
    first_chr_num = ord(first)
    second_chr_num = ord(second)
    final_string = ""

    for character in range(first_chr_num + 1, second_chr_num):
        final_string += chr(character) + " "

    return final_string

first_character = input()
second_character = input()

print(chatacters_in_range(first_character, second_character))
