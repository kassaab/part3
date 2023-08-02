word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = word.find(char)
size = len(word)

while size > index + 2:
    if index < 0:
        break
    print(word[index:index+3])
    word = word[index+1:]
    index = word.find(char)
    size = len(word)