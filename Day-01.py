# print("hello world") #testing python is installed or not

# statements
# print("this is a statement in python")
# using semicolons in python (optional and rarely used)
# print("hello"); print("hello2"); print("hello3")
# double or single quotes
# print("hello world")
# print('hello world single quotes')
# print usually ends in new line ( want to use multiple prints but still want to display in same line )
# print("first line", end=" ")
# print("contiuning first line")
# variables
person_name = "prasxor"
person_age = 1000
# print("name datatype: ", type(person_name),"age datatype: ", type(person_age))
# variables names techniques 
# camel case 
# myVariableName = "John"
#Pascal Case
# MyVariableName = "John"
#Snake case
# my_variable_name = "John"
# ilegal variable name 
# my-var = 20 ( ' - ' is not allowed between the variables declare)
# assigning multiple values 
# x,y,z = "apple", "boy", "cat"
# print(x,y,z)

# one value to multiple variables 
# a = b = c = "orange"
# print(a)
# print(b)
# sometimes comma(,) work as space between printing statements 
# print("hello", "world")

#global variables 
# ( we can create a outer function variable and use it in function but when we create same variable inside function then most preferences given to local variable not global variable and we can't use inside variable at outside of the function )
x = "apple"

def myfunc():
    x = "mango"
    print("I like " + x)
    
myfunc()
print(x)
# datetypes
# 1. str
# 2. int
myint = 10e100 #also supports scientific numbers like 'e'
print(myint)
print(int(myint))
# 3. complex
# 4. list
# 5. tuple
# 6. range
y = range(101)
print(y)
print(list(y))
print(tuple(y))
print(type(y))

# 7. dict
z = {"name": "prashant", "age": 36}
print(z)

# 8. set
mySet = {"name", "hello", "got"}
print(type(mySet))

#9. frozenset
myfrozen = frozenset(("hello", "world", "set"))
print(type(myfrozen))

#10.bool
#11. None
mynone = None
print(type(mynone))
#python casting
#int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#strings 
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'