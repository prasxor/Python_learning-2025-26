class A:
    def display_A(self):
        print("A class method")
        
class B(A):
    def display_B(self):
        print("B class method")
        
class C:
    def display_C(self):
        print("C class method")
        
class D(B,C):
    def display_D(self):
        print("D class method")
        
a1 = A()
# a1.display_A()

b2 = B()
# b2.display_A()
# b2.display_B()

c1 = C()
# c1.display_C()

d1 = D()
d1.display_A()
d1.display_B()
d1.display_D()
d1.display_C()

# MRO - method resolution order : It is going to return the flow of hte inheritance of each class
# syx : ClassName.__mro__ 
# it is used to know that which class is inheriting to which class to know the order of inheritances 

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)

