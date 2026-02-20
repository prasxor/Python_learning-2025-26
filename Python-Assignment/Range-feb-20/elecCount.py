userInput = eval(input("Enter your value to count the elements: "))

try:
    value = eval(userInput)
except:
    value = userInput

count = 0
if type(userInput) in (str,list,tuple,set,dict):
        for i in userInput:
            count +=1
else:
    print("We can't count the numbers on primitive datatype")
    
print(count)