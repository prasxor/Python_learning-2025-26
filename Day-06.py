# python *args and **kwargs 
# However, sometimes you may not know how many arguments that will be passed into your function
# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name

def my_function(*kids):
    print("the youngest child is "+ kids[2])

my_function("rahul", "prashant", "shantanu")

# what is *args 

def my_function1(*args):
    print("type of", type(args))
    print("first argument: ", args[0])
    print("second argument: ", args[1])
    print("all argument: ", args)


my_function1("hello", "bye", "nice")

# using *args with regular arguments 

def my_function2(greetings, *name):
    for i in name:
        print(greetings, i)
        
naam = ["prashant", "kumar", "sinha"]  #hello ['prashant', 'kumar', 'sinha']
my_function2("hello", naam, "rahul", "shantanu")

# sum in function using *args 

def addition_of_sum(*args_values):
    total = 0
    for current_values in args_values:
        total += current_values
    return total

summing = addition_of_sum(10,20,30,40,50,60,70)
mylist_sum = [10,20,30,40,50,60,70]
print(addition_of_sum(*mylist_sum))
print(summing)

# finding the max_value using *args

def my_function_for_max_values(*values):
    if len(values) == 0:
        return None
    max_value = 0
    for current_value in values:
        if current_value> max_value:
            max_value = current_value
    return max_value


print(my_function_for_max_values(1,2,3,4,5,2,3,22,3,4,33,4,5,333,2,876,23))

# finding the min value using *args

def my_function_to_find_min_value(*values):
    if len(values) == 0:
        return None
    min_value = float('inf')
    for current_value in values:
        if current_value < min_value:
            min_value = current_value
    return min_value
    
min_values_list = [11,2,3,4,5,2,3,22,3,4,33,4,5,-1,333,2,876,23]
print(my_function_to_find_min_value(*min_values_list))

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# its creates the dictionary key and value pair in args as in *args we created tuple

def my_function4(**kids):
    print("his last name is " +kids['lname'])

my_function4(fname="prashant", lname="sinha")

def my_function6(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function6(name = "Tobias", age = 30, city = "Bergen")

def my_function5(username, **details):
    print("username: ", username)
    for key,value in details.items():
        print(key, ":", value)
        
my_function5("prashant", city="hyd", age= 22, hobby="coding")

# combing regular parameters,*args, **kwargs

def mix_function(name, *arg, **kwargs):
    print("username", name)
    print("*args: ", arg)
    print("*kwargs: ", kwargs)
    
mix_function("prashant", 'kya', 'bolu', age=12, city='hyd', )

# unpacking list with *
mylist_sum = [10,20,30,40,50,60,70]
print(addition_of_sum(*mylist_sum))

# unpacking dictionaries with **

my_dict = {
    'city': 'hyderabad',
    'age': 21,
    'gender': 'male'
}

my_function5("prashant", **my_dict)

# scope 
# a variable is only available from inside the region it is created. This is called scope 

# local scop 

def myfunc():
    x = 20
    print(x)
    
myfunc()

# nested function 

def myfunc_main():
    x = 300
    def myinner_func():
        print(x)
    myinner_func()

myfunc_main()

x = 301

def myfunc2():
    print(x)
    
myfunc2()

print(x)

# global keyword 

def myfunc_global():
    global xy
    xy = 400


# print(xy)
myfunc_global()
print(xy)


print(x)

def myfunc():
  global x
  x = 200

myfunc()

print(x)

def myfunc1():
  xx = "Jane"
  def myfunc2():
    nonlocal xx
    xx = "hello"
  myfunc2()
  return xx

print(myfunc1())

# python decorators 

# sample for youtube 

def div1(a,b):
    print(a/b)
    
div1(2,4)
div1(4,2)
# the above function is not in your control to change or you can't make changes as per company rule, but the problem is the first arg should be greater then second arg cause it diving as we need (4,2) which returns 2.0, if we have (2,4) then its returns 0.5 which is not we want we want that greater value should be 1st arg
#without touching the exist function using decorators 

def newfunc(funcName):
    
    def inner(a,b): #this innerfunction should have same no.of paramenter as your div or targetted function
        if a<b:
            a,b = b,a # we just swapped the values if a is less then b, so we get larger value at (a) which is positional first parameter
        return funcName(a,b) # no.of same parameter in inner func
    return inner

@newfunc # decorator should be above the function
def div(a,b):
    print(a/b)
    
    
div(2,4)
div(4,2)

# call counter to know how many times function as been runned 
# chatgpt question

def counter(func):
    timer = 0
    def inner(*args):
        nonlocal timer
        timer += 1
        # print(a+b)
        print("results are runned: ", timer)
        return func(*args)
    return inner

@counter
def summary(a,b):
    print(a+b)
    
summary(10,2)

# example from w3school 

# def changeCase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changeCase
# def myfunction():
#     return "hello world"

# print(myfunction())

# mutiple decorator calls 

def changeCase(func):
    def myinner():
        return func().upper()
    return myinner

@changeCase
def myfunction():
    return "hello world"

@changeCase
def anotherMyfunc():
    return "bye bye"

print(myfunction())
print(anotherMyfunc())

# arguments in the decorated function 

def changingCase(func):
    def innerfunc(x):
        return func(x).upper()
    return innerfunc

@changingCase
def merijaan(nam):
    return "your name is : " + nam

print(merijaan("prashant"))
# def changecase(func):
#   def myinner(x):
#     return func(x).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return "Hello " + nam

# print(myfunction("John"))

# decorator with arguments 

def caseChanger(n):
    def caseChanges(funct):
        def innerfunc():
            if n == 1:
                a = funct().lower()
            else:
                a = funct().upper()
            return a
        return innerfunc
    return caseChanges

@caseChanger(1)
def myFuncing():
    return "Hello prashant"

print(myFuncing())

# multiple decorators 

def uperCasing(func):
    def innerfunc():
        return func().upper()
    return innerfunc

def greetingsfunc(func):
    def innerfunc():
        return "Hey buddy " + func()
    return innerfunc

@uperCasing
@greetingsfunc
def details():
    return "Prashant"

print(details())


# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

def myfu():
    return "have nice day"

print(myfu.__name__)
print(myfu.__doc__)