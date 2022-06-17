text = input()

vowels = ["a", "o", "u", "i", "e", "A", "O", "U", "I", "E"]
no_vowels = "".join([chr for chr in text if chr not in vowels])
print(no_vowels)
