from Bank import Bank

class Sbi(Bank):
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def checkBalance(self):
        print(f"Hey {self.name}, your current balance is {self.balance}")
    
    def deposit(self, amount):
        if self.balance>=0:
            self.balance += amount
            print(f"Rs:{amount} is credited to your account and your current balance is {self.balance}")
        else:
            print("invalid amount on the account")
            
    
    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance -= amount
            print(f"Rs:{amount} debited from your account and your current balance is {self.balance}")
        else:
            print("insufficient balance")
            
# c1 = Sbi("prashant", 1000000)
# c1.checkBalance()
# c1.deposit(200000)
# c1.withdraw(1)