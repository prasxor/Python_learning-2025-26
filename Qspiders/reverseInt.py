# without typecasting

n1= 555
n=n1
rev = 0
while n>0:
    last = n%10
    rev = rev*10+last
    n = n//10
    
if n1==rev:
    print("palindrome")
else:
    print("non - palindrome")


# with typecasting

# n = str(n)
# n = n[::-1]
# print(n)