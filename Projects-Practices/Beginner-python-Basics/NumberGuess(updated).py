'''
I want that guess should be done ones and user need to guess where system helps to admire the less or greater with the computer guessed number, every choice make reduction in choice
'''

import random

sysGuess = random.randint(1,20)
choice = 5
computerScore = 0
userScore = 0

while True:
    userInput = str(input("Enter your guess between 1 to 20: "))
    if len(userInput) == 0:
        print("Enter valid or some number on it")
    else:
        userInput = int(userInput)
        if userInput == 00:
                break
        if userInput > sysGuess:
                print("Your guessed number is greater, pick any smaller number")
                choice -= 1
                print(f"you have {choice} left")
        elif userInput<sysGuess:
                print("Your guessed number is smaller, pick any greater number")
                choice -= 1
                print(f"you have {choice} left")
        elif userInput == sysGuess:
                print("Your guessed was right")
                userScore += 1
                choice = 5
                print(f"Your Score : {userScore}\nComputer Score : {computerScore}")
        else:
                print("Please enter valid number between 1 to 20")
    if choice == 0:
        print("You run out of choice")
        computerScore += 1
        print(f"Your Score : {userScore}\nComputer Score : {computerScore}")
        choice = 5
        break
        