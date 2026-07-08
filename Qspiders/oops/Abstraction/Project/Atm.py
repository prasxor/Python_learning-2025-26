from Sbi import Sbi

print('''
    Welcome to the Sbi bank
    press option to choose
    1. create new account
    2. check existed balance
    3. deposit the amount
    4. withdraw the amount
    5. exit
    ''')

while True:
    userChoice = int(input("Enter your choice from options: "))
    if userChoice == 1:
        userName = str(input("Enter your name: "))
        userPin = int(input("Enter your account pin: "))
        