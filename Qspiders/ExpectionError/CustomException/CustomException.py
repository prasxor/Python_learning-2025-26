username = 'prashant'
password = 9876

class PasswordError(Exception):
    pass

class UsernameError(Exception):
    pass

userInput = str(input("Enter your username: "))
userPass = int(input("Enter your password: "))

if userInput == username:
    
    if userPass == password:
        print(f"Welcome back, {username}")
    else:
        raise PasswordError("Password is invalid")
else:
    raise UsernameError("Username is invalid")