from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def checkBalance(self):
        pass
    
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
