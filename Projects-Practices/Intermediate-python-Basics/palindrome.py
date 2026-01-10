# Check whether a given string is a palindrome.

userInput = str(input("Enter your name: "))
userInput = userInput.strip("")
if userInput.lower() == userInput[::-1].lower():
    print('Given word is palindrome')
else:
    print("given Word is not palindrome")