# Counting the no.of digit in int value without len() or typecasting 

x = 3454575
last = 0
count = 0

while x>0:
    last = x/10
    count += 1
    x = x//10

print(count)