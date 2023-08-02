string = input("Please type in a string: ")
length = len(string)
num = 0

while length >= 0:
    print(string[length:])
    length -= 1