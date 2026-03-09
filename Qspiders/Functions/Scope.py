# x = 10

# def basic():
#     x = 100
#     x+=200
#     print(x)

# basic()
# x+=10
# print(x)

x = 10

def basic():
    global x
    y = 0
    x+=200
    # print(x)
    def nestedBasic():
        nonlocal y
        y += 1000
        print(y)
    y+=500
    nestedBasic()

basic()
x+=10
print(x)
basic()