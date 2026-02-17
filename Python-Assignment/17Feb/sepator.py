# check the char is uc/lc/digit/spcl char [elif]

# uc -> convert -> lc and add it to a string 
# lc -> convert -> uc and add it to a list
# # digit -> create a key a digit and value as square num 
# spcl -> add it to tuple 


userInput = str(input("Enter your character: "))
txt = ''
listly = []
tuply = tuple()
dictly = {}

if userInput.isupper():
    userInput = userInput.lower()
    txt += userInput
elif userInput.islower():
    userInput = userInput.upper( )
    listly.append(userInput)
elif userInput.isdigit():
    dictly[userInput] = int(userInput)**2
else:
    tuply = userInput

print("the txt var is ", txt)
print("the listly var is ", listly)
print("the tuply var is ", tuply)
print("the dictly var is ", dictly)