from Sbi import Sbi

def customUserNameCreator(name,pin):
    cname = set(name)
    cname = str(customUserNameCreator)
    pin = str(pin)
    pin = pin[-1:-2:-1]
    return (name + pin)
    
userDict = dict()


while True:
    print('''
    Welcome to the Sbi bank
    press option to choose
    1. create new account
    2. check existed balance
    3. deposit the amount
    4. withdraw the amount
    5. exit
    ''')
    
    userChoice = int(input("Enter your choice from options: "))
    if userChoice == 1:
        userName = str(input("Enter your name: "))
        userPin = int(input("Enter your account pin: "))
        balance = 0
        Cid = customUserNameCreator(userName,userPin)
        cid = Sbi(userName, balance)
        
        print(f"{userName} your account as been created and your current balance is {balance}")
    elif userChoice == 2:
        CheckUsername = 