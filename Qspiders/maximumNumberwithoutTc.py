# finding the maximum number without using typecasting 

x = 3458374
maxNum = float('-inf')
currentMax = 0
while x>0:
    currentMax = x%10
    if currentMax>maxNum:
        maxNum = currentMax
    x = x//10
        
print(maxNum)