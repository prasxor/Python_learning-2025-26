
d = {"a": 1}

userInput = input("Enter 'a' or 'b': ")
# b -> 1
# a -> 2

if userInput in d:
    d[userInput] += 1
else:
    d[userInput] = 1
    
print(d)