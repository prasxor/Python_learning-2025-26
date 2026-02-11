userInput = int(input("Enter your age: "))

if(userInput>=1 and userInput<=13):
    print("Child")
elif(userInput>13 and userInput<=19):
    print("Teenager")
elif(userInput>=20 and userInput<=64):
    print("Adult")
elif(userInput>=65):
    print("Senior")
else:
    print("Enter the correct age")