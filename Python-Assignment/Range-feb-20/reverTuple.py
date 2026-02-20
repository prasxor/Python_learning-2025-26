myTuple = (1,2,3,4,5,6)
newTuple = tuple()

for i in range(len(myTuple)-1, -1,-1):
    newTuple += (myTuple[i],)
    
    
print(newTuple)