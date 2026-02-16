# total sum of integer value without typecasting 

x = 3456
last = 0
result = 0

while x>0:
    last = x%10
    result = result*1+last
    x = x//10

print(result)