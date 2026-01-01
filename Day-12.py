# python virtual environment
# creation is : python -m venv myfirstproject

#  source myfirstproject/bin/activate
# pip install cowsay
# python test.py
# deactivate
# to delete : rm -rf myfirstproject

# OOP
# what are classes and objects 

# python classes and objects 

class MyClass:
    x = 5
    
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)
# del p1

# pass statement 

# class Person:
#     pass

# python __init__() method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
p1 = Person("Emil", 26)  

print(p1.name)
print(p1.age)

# without __init__ method

class Person1:
    pass

p1 = Person1()
p1.naam = "hello"
p1.umar = 35

print(p1.naam)
print(p1.umar)


p3 = Person("linus", 30)
print(p3.name)
print(p3.age)

# why use self 

class Car:
    def __init__(self,name):
        self.name = name
    
    def printname(self):
        print(self.name)
        
        
p1 = Car("lambo")
p2 = Car("BMW")

p1.printname()
p2.printname()


# accessing properties with self 
class Cars:
    def __init__(self, Cname, Cmodel):
        self.Cname = Cname
        self.Cmodel = Cmodel
        
    def PrintName(self):
        print(f"{self.Cname} and {self.Cmodel}")
        
        
car1 = Cars("BMW", "i7")
car1.PrintName()

# greeting example 

class Person:
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        return "Hello " + self.name
    
    def welcome(self):
        message = self.greeting()
        print(message , "Welcome to our website")
    
newPerson = Person('prashant')
newPerson.welcome()