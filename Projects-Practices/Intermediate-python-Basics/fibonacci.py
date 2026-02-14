# Generate the first n numbers of the Fibonacci sequence.

i = 0
a= 0
b=1

while i<=10:
    calculate = a+b
    a = b
    b = calculate
    print(calculate)
    i+=1