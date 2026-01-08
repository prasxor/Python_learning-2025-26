# Take a sentence as input and count the number of words.

while True:
    userInput = str(input("Enter your sentences to count the words: "))
    if len(userInput)> 0:
        break
    else:
        print("Please, Enter something or valid sentence")

mylist = userInput.split()
result = len(mylist)
print(f"Total words presents in the sentence is : {result}")