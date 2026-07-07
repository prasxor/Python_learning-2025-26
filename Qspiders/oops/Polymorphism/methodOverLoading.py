# class Sample:
#     def add(self, a,b):
#         print(a+b)
        
#     def add(self,a,b,c):
#         print(a+b+c)
        
# c1 = Sample()
# # c1.add(1,2) # missing argument
# c1.add(1,2,3) #6


# PARTIAL METHOD OVERLOADING WITH DEFAULT PARAMETER 

class Sample:
    def add(self,a=0, b=0,c=0):
        print(a+b+c)
    
s1 = Sample()
s1.add(1,2,3)
s1.add(1,2)
s1.add(1)