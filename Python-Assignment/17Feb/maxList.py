x = [1,4,6,2,5,2,23]
max = float("-inf")
i = 0

while i<=(len(x)-1):
    if x[i]>max:
        max = x[i]
    i+=1

print("max number is:", max)