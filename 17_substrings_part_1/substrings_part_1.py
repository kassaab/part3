string = input("Please type in a string: ")
length = len(string)
num = 1

while num <= length:
    print(string[0:num])
    num += 1