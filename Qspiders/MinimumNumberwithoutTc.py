# finding the Minimum number without using typecasting 

x = 34502184
minNum = float('+inf')
currentMin = 0

while x>0:
    currentMin = x%10
    
    if currentMin<minNum:
        minNum = currentMin
        
    x= x//10

print(minNum)