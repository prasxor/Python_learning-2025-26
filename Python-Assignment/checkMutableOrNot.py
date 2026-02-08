userInput = eval(input("Enter your value to know the datatype: "))

# print(type(userInput))
# primitiveDt = [int,float,complex,bool,None]

mutableDt = [list,dict,set]

print("This is Mutable Data Type") if type(userInput) in mutableDt else print("This is Immutable Data Type")
