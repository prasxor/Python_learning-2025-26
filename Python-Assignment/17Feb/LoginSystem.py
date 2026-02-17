userName = input("Enter your user name: ")

registeredUserName = "deva sir"
registeredPass = "python@1"

if userName == registeredUserName:
    password = input("Enter your Password: ")
    if password == registeredPass:
        print("login successful")
    else:
        print("Wrong password")
else:
    print("user not found")