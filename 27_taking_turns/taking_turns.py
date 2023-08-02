num = int(input("Please type in a number: "))
i = 1

while i < num:
    print(i)
    print(num)
    i += 1
    num -= 1
if i == num:
    print(num)