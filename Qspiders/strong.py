n = input("Enter your number to know strong or not: ")

def factorial(n):
    n = abs(n)
    if n==1 or n==0:
        return 1
    else:
     return n * factorial(n-1)

curr = []
s = 0
end = len(n)-1

while s<= end:
    curr.append(factorial(int(n[s])))
    j = 0
    sum = 0
    while j<=(len(curr)-1):
        sum += curr[j]
        j+=1
    s+=1

if n == str(sum):
    print("It is strong")
else: 
    print("It is not strong")

# print(curr)
# print(sum)  