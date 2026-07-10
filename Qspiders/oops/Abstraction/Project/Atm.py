from Sbi import Sbi

def customUserNameCreator(name,pin):
    cname = set(name)
    cname = str(customUserNameCreator)
    pin = str(pin)
    pin = pin[-1:-2:-1]
    return (name + pin)
    
userDict = dict()
globalBalance = 0

while True:
    print(f'''
    Welcome to the Sbi bank
    ------------------------
    press option to choose
    ------------------------
    1. create new account
    2. check existed balance
    3. deposit the amount
    4. withdraw the amount
    5. exit
    ''')
    
    userChoice = int(input("Enter your choice from options: "))
    if userChoice == 1:
        userName = str(input("Enter your name: "))
        while True:
            print("Create a new pin")
            userPin = int(input("Enter your account pin: "))
            print("Confirm your pin")
            confirmUserPin = int(input("Enter your account pin: "))
            if userPin == confirmUserPin:
                balance = 0
                balance = globalBalance
                # cid = customUserNameCreator(userName,userPin)
                global cid = Sbi(userName, balance)
                print(f"{userName} your account as been created and your current balance is {balance}")
                # userDict[userName] = confirmUserPin
                userDict.setdefault(userName, confirmUserPin)
                userDict[userName]["account"]
                break
            else:
                print("pin is incorrect, create again")
                break
    elif userChoice == 2:
        checkUsername = str(input("Enter your user name : "))
        if checkUsername in userDict:
            print(f"Welcome {checkUsername}")
            checkPin = int(input("Enter your pin: "))
            if checkPin == userDict[checkUsername]:
                print("Login successful")
                print(f"your current balance is Rs:{globalBalance}")
                # .checkBalance()
            else:
                print("pin is incorrect, try again")
        else:
            print("username is not found, create new account")
    elif userChoice == 3:
        checkUsername = str(input("Enter your user name : "))
        if checkUsername in userDict:
            print(f"Welcome {checkUsername}")
            checkPin = int(input("Enter your pin: "))
            if checkPin == userDict[checkUsername]:
                print("Login successful")
                cid.deposit(10000)
                
                # print(f"your current balance is Rs:{globalBalance}")
                
            else:
                print("pin is incorrect, try again")
        else:
            print("username is not found, create new account")
    else : 
        pass