# 2.	Print numbers from 1 to 100 with the following rules:
# 		•	Print Fizz for multiples of 3
# 		•	Print Buzz for multiples of 5
# 		•	Print FizzBuzz for multiples of both

i = 1
while i<=100:
    if (i%3 and i%5 == 0):
        print(i, "FizzBuzz")
    else:
        if i%3==0:
            print(i, "Fizz")
        elif i%5 == 0:
            print(i, "Buzz")
    i+=1
    