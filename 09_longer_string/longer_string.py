string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")
len1 = len(string1)
len2 = len(string2)

if len1 > len2:
    print(f"{string1} is longer")
elif len1 < len2:
    print(f"{string2} is longer")
else:
    print("The strings are equally long")