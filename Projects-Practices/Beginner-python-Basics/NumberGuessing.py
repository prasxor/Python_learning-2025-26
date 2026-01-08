# Generate a random number between 1 and 20 and create a number guessing game.

import random

print("Hit the score 10 and WON")
computerWon = 0
Userwon = 0

while True:
    guessedNumber = random.randint(1,20)
    print("Press '00' for exit")
    print(f'''Your Score : {Userwon}
Computer Score : {computerWon}''')
    userinput = str(input("Guess the number: "))
    if len(userinput) == 0:
        print("Enter something")
    else:
        userinput = int(userinput)
        if userinput == 00:
            break
        elif userinput>20:
            print("Please, guess valid number between 1 to 20")
        elif userinput == guessedNumber:
            print(f"Computer guessed the {guessedNumber} and Right guess")
            Userwon += 1
            if Userwon== 10:
                print(f"You Won with score {Userwon-computerWon}")
                break
        else:
            print(f"Computer guessed the {guessedNumber} and wrong guess")
            computerWon += 1
            if computerWon == 10:
                print(f"You Lose with score {computerWon-Userwon}")
                break