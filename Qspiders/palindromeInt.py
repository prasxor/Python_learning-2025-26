x = 3433543
x1 = x
last = 0
resDigit = 0

while x>0:
    last = x%10
    resDigit = resDigit*10+last
    x = x//10

if x1 == resDigit:
    print("It is palindrome")
else:
    print("It is not a palindrome")
