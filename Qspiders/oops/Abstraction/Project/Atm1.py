from Sbi import Sbi


    

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
    
    userChoice = int(input("Enter your option: "))
    
    if userChoice >= 1 and userChoice <=5:
        userName = str(input("Enter your name: \n"))
        if userChoice == 1:
            password = int(input())
    
    
    
c1 = Sbi("prashant kumar sinha",20000)
c1.checkBalance()
# c1.withdraw(1000)