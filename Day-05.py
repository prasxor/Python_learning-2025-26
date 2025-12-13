# Python match 

day = 6

# match day:
#     case 1 :
#         print("its monday")
#     case 2:
#         print("its tuesday")
#     case 3:
#         print("its wednesday")
#     case 4:
#         print("its thursday")
#     case 5:
#         print("its friday")
#     case 6:
#         print("its saturday")
#     case 7:
#         print("its sunday")
#     case _:
#         print("its no day")

match day:
    case 1 | 2| 3| 4|5:
        print("its weekday")
    case 6|7:
        print("its weekend")
        
# if statement in match

day = 3
month = 5


match day:
    case 1 | 2|3|4|5|6 if month== 4:
        print("its january")
    case 1|2|3|4|5 if month==5:
        print("its feburary")
    case _:
        print("its backup error baby")
        
        
# python loops - two primitive loop while and for loops

# while loop 

# i = 0

# while i < 6:
#     print(i)
#     i +=1
    
# break statement 

# while i<6:
#     print(i)
#     if i ==3:
#         break
#     i += 1

#contiune statement
# i = 0
# while i<6:
#     print(i)
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# else in loop 

# j = 1

# while j<6:
#     print(j)
#     j+=1
# else:
#     print("j is no longer less then 6")

# for loop

fruits = ["apple", "banana", "cherry"]
# # loop through list 
# for i in fruits:
#     print(i)

# looping through string 

# hlo = "string"

# for i in hlo:
#     print(i)
    
# the break statement 

# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
    
# the continue statement 
# for x in fruits:
#     print(x)
#     if x== "banana":
#         continue
#     print(x)
    
# range 

# for i in range(10):
#     print(i)
    
# for j in range(3,10):
#     print(j)

# else in for loop 

# for x in range(2,11):
#     print(x)
# else:
#     print("finally finished!")
    
# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# for x in range(6):
#   if x == 3: 
#       break # when we use break its not executed else block
#   print(x)
# else:
#   print("Finally finished!")
  
adj = ["red", "big", "tasty"]
fruits1 = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits1:
#         print(x,y)

for x in [0,1,2]:
    pass # its uses to keep it empty for futher logic without error

# python functions 

def my_function():
    print("hello from function")
    
my_function()

def celisusData(temp):
    return (temp - 32) * 54/9

print(celisusData(108))

# pass in function 

def another_myFunc():
    pass

# python function arguments 
# difference between parameter vs argument
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# default parameter values 
def my_function1(name = "friend"):
    print("hello", name)

my_function1("payal")
my_function1()


# keyword arguments

def personalDetails(name, age,course="unknown"):
    print(f"hlo, I'm {name} and I'm {age} years old and in {course}")

personalDetails(age=21, name="prashant", course="bca") #argument order not matter when you use parameter variable in argument

# positional arguments 

personalDetails("prashant", 21, course="bcom")

# return values 

# def my_function(x, y):
#   return x + y

# result = my_function(5, 3)
# print(result)

def myfunction():
    return [1,2,3,4]

fruits = myfunction()
print(fruits[0]) # we can access the function list using index after assigning