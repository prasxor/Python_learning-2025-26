# Take a string input and reverse it without using slicing.

userString = input("Enter your string : ")

i = -1
newlist = []

while i >= -abs(len(userString)):
    newlist.append(userString[i])
    i -= 1

reservedString = "".join(newlist)
print(f'The reserved of {userString} is {reservedString}')