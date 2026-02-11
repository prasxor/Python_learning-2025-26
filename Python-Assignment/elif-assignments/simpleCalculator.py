print('Welcome to Simple calculator')

firstValue = float(input("Enter your first value: "))
secondValue = float(input("Enter your second value: "))

print('''
      press '+' for addition
      press '-' for subtraction
      press '*' for multiplication
      press '/' for division
      ''')

userOperator = input("Enter your operator: ")

if(userOperator== "+"):
    print(f"Sum of two numbers are {firstValue+secondValue}")
elif(userOperator=='-'):
    print(f"minus of two numbers are {firstValue-secondValue}")
elif(userOperator=='*'):
    print(f"multiply of two numbers are {firstValue*secondValue}")
elif(userOperator=='/'):
    print(f"Division of two numbers are {firstValue/secondValue}")
else:
    print("Invalid Operator")