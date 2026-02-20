myList = [1,2,3,4,5,6]
newList = list()

for i in range(len(myList)-1, -1, -1):
    newList.append(myList[i])
    
print(newList)