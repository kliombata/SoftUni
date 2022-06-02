start_number = int(input())
end_number = int(input())

string = ""

for i in range(start_number, end_number + 1):
    string += chr(i) + " "

print(string)
