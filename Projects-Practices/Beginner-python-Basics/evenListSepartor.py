# Given a list of integers, filter and print only the even numbers.

alllist = [1,23,4,5,23,63,63,13,67,33,98,23,29,2]
evenList = []
for i in alllist:
    if i%2 == 0:
        evenList.append(i)
    
print(evenList)