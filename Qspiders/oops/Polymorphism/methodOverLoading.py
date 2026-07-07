# class Sample:
#     def add(self, a,b):
#         print(a+b)
        
#     def add(self,a,b,c):
#         print(a+b+c)
        
# c1 = Sample()
# # c1.add(1,2) # missing argument
# c1.add(1,2,3) #6


# PARTIAL METHOD OVERLOADING WITH DEFAULT PARAMETER 

# class Sample:
#     def add(self,a=0, b=0,c=0):
#         print(a+b+c)
    
# s1 = Sample()
# s1.add(1,2,3)
# s1.add(1,2)
# s1.add(1)

# TUPLE VARIABLE ARGUMENT
class Sample:
    def add(self, *args):
        total = 0
        for i in args:
            total +=i

        return total
    
s1 = Sample()
res = s1.add(1,2,3)
print(res)
print(s1.add(1,2,3,4,5,5,6,7,7,88,))