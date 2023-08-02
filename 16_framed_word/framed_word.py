word = input("Word: ")
length = int((30 - len(word)) / 2 - 1) #the amount of white space before and after 'word'

print("*" * 30)
if len(word) % 2 == 0:
    print("*" + " " * length + word + " " * length + "*")
else:
    print("*" + " " * length + word + " " * length + " " + "*")
print("*" * 30)