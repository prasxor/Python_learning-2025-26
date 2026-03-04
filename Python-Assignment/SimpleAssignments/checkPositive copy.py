userInput = int(input("Enter your value to know the +ve or -ve: "))

def positiveOperation(val):
    result = val//10
    print(f"This is a positive number and output is : {result}")

positiveOperation(userInput) if userInput > 0 else print("This is a negative (-ve) number")